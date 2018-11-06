import grammar


def title_item(item):
    given_name = item.TreasureLabel
    core_name = item.TreasureType.lower()

    if item.material:
        core_name = " ".join([item.material.__adj__.lower(), core_name])

    adjs = item.adjectives
    if adjs:
        name = " ".join([grammar.sequence_words(adjs), core_name])
    else:
        name = core_name

    if given_name:
        return given_name + ", the " + name
    else:
        return grammar.get_a(name, include=True)


def item_description(item, *, top=True, minimal=False, recursive=True):
    components = item.dictComp
    rail = "|" if components and recursive else " "
    line_out = [title_item(item)]

    if top:
        line_out[0] = "This is " + line_out[0] + "."

    try:
        # See if it is a weapon object
        d = item.calc_damage()
        dsum = round(sum(d), 2)
        wgh = item.weight()
        spd = item.speed()
        line_out += [
            f"{rail}> It does {str([round(i, 2) for i in d])} C/P/S damage for {str(dsum)} ideal-total.",
            f"{rail}> It has a weight of {str(wgh)} for a speed of {str(spd)}.",
            f"{rail}> It does {str(round((dsum + spd) / 10, 2))} DPS.",
        ]
    except AttributeError:
        pass

    try:
        # See if it is part of a weapon object
        d = item.damage_rating()
        dstr = [str(n) for n in d]
        if sum(d) > 0:
            line_out.append(
                f"{rail}+ It contributes {dstr} C/P/S damage to its parent."
            )
    except AttributeError:
        pass

    if not minimal:
        # If the function was not told to be minimal, return a few more lines of flavor text
        traits = item.dictTrait
        attributes = item.dictAttr
        additional = item.dictAdd
        adjectives = item.get_adj()

        # Print object adjectives as a single line
        if adjectives:
            line_out.append(f"{rail}! It is {grammar.sequence_words(adjectives)}.")

        # Print object attributes (variable number)
        for a, v in attributes.items():
            description = grammar.sequence_words(v)
            if description != "":
                line_out.append(f"{rail}= Its {a.lower()} is {str(description)}.")

        # Print object traits (one of each)
        for a, v in traits.items():
            line_out.append(f"{rail}- Its {a.lower()} is {grammar.sequence_words(v)}.")

        # Print object embellishments (one of each, as passive verbs)
        for a, v in additional.items():
            line_out.append(f"{rail}* It {v.as_pverb()}.")

    if recursive:
        for i, v in enumerate(components.items()):
            line_out.append("|")
            prefix_first, prefix_rest = (
                ("\\_", "  ") if i == len(components) - 1 else ("|_", "| ")
            )
            ret = item_description(
                v[1], top=False, minimal=minimal, recursive=recursive
            )

            line_return = [
                prefix_first + "[{}] Its {} is {}.".format(i, v[0].lower(), ret.pop(0))
            ]
            line_return += [prefix_rest + line for line in ret]
            line_out += line_return

    return line_out


def describe_item(item, minimal=False, norecurse=False):
    line_in = item_description(item, minimal=minimal, recursive=not norecurse)
    line_out = "\n".join(line_in)
    print("\n" + line_out + "\n")
