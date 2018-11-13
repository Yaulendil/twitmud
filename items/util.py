import grammar

# Characters to use for the tree/rail.
# LINE = [" ", "|", "\\", "|", "_"]
# LINE = [" ", "║", "╙", "╟", "╼"]
# LINE = [" ", "│", "╘", "╞", "═"]
LINE = [" ", "│", "╰", "├", "╼"]
# In order: Empty, rail without entry, final entry, rail with entry, entry

Colorful = False


def longest_in_list(_list):
    longest = 0
    for x in _list:
        if len(x) > longest:
            longest = len(x)
    return longest


def combine_images(imgs, joint=" "):
    longest = longest_in_list(imgs)
    for img in imgs:
        while len(img) < longest:
            img.append(" " * longest_in_list(img))
    img_composite = [joint.join([p[i] for p in imgs]) for i in range(longest)]
    # return "\n".join(img_composite)
    return img_composite


def title_item(item):
    if not item:
        return "nothing"

    core_name = item.TreasureType.lower()
    given_name = item.TreasureLabel

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


def item_image(item):
    line_out = []
    for v in item.dictComp.values():
        line_out += getattr(v, "image", [])
    return line_out


def wrap_text(text, indent, limit=50):
    for i, line in enumerate(text):
        if len(line) > limit:
            text[i:i+1] = [line[:limit] + "-", " " * indent + "-" + line[limit:]]


def item_description(item, *, top=True, minimal=False, recursive=True, lineset=LINE):
    """Return a list of strings, which, when join()ed by '\n's, display hierarchy"""
    components = getattr(item, "dictComp", None)
    rail = lineset[1] if components and recursive else lineset[0]
    line_first = title_item(item)
    line_out = []

    if top:
        line_first = "This is " + line_first + "."

    if item:
        try:
            # See if it is a weapon object
            d = item.calc_damage()
            dsum = round(sum(d), 2)
            wgh = item.weight()
            spd = item.speed()
            line_out += [
                f"> It does {str([round(i, 2) for i in d])} C/P/S damage for {str(dsum)} ideal-total.",
                f"> It has a weight of {str(wgh)} for a speed of {str(spd)}.",
                f"> It does {str(round((dsum + spd) / 10, 2))} DPS.",
            ]
        except AttributeError:
            pass

        try:
            # See if it is part of a weapon object
            d = item.damage_rating()
            dstr = [str(n) for n in d]
            if sum(d) > 0:
                line_out.append(
                    f"+ It contributes {dstr} C/P/S damage to its parent."
                )
        except AttributeError:
            pass

        if not minimal:
            # If the function was not told to be minimal, return a few more lines of flavor text
            traits = item.dictTrait
            attributes = item.dictAttr
            additional = item.decor
            adjectives = item.get_adj()

            # Print object adjectives as a single line
            if adjectives:
                line_out.append(f"! It is {grammar.sequence_words(adjectives)}.")

            # Print object attributes (variable number)
            for a, v in attributes.items():
                description = grammar.sequence_words(v)
                if description != "":
                    line_out.append(f"= Its {a.lower()} is {str(description)}.")

            # Print object traits (one of each)
            for a, v in traits.items():
                line_out.append(f"- Its {a.lower()} is {grammar.sequence_words(v)}.")

            # Print object embellishments (one of each, as passive verbs)
            for v in additional:
                line_out.append(f"* It {v.as_pverb()}.")

    wrap_text(line_out, 3, 60)

    line_out = [rail + line for line in line_out]
    if line_first:
        line_out[0:0] = [line_first]

    if recursive and components:
        for i, v in enumerate(components.items()):
            line_out.append(lineset[1])
            prefix_first, prefix_rest = (
                (lineset[2] + lineset[4], lineset[0] * 2)
                if i == len(components) - 1
                else (lineset[3] + lineset[4], lineset[1] + lineset[0])
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


def describe_item(item, minimal=False, norecurse=False, images=False):
    line_in = item_description(item, minimal=minimal, recursive=not norecurse)
    if images:
        img_in = item_image(item)

        while len(img_in) < len(line_in):
            img_in.append("       ")
        while len(line_in) < len(img_in):
            line_in.append("")

        all_in = [" ".join(["", img_in[i], line_in[i]]) for i in range(len(img_in))]
    else:
        all_in = line_in

    line_out = "\n".join(all_in)
    print("\n" + line_out + "\n")
