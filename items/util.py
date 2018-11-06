from grammar import sequence_words
from items import treasure_core

def title_item(item):
    return item.strself()


def item_description(item, top=True, minimal=False, recursive=True):
    components = item.dictComp
    line_out = [title_item(item)]

    if top:
        line_out[0] = "This is " + line_out[0]

    if not minimal:
        # If the function was not told to be minimal, print a few more lines of flavor text
        traits = item.dictTrait
        attributes = item.dictAttr
        additional = item.dictAdd
        adjectives = item.dictAdj
        rail = "|" if components else " "

        # Print object adjectives as a single line
        if adjectives:
            line_out.append(f"{rail}# It is {sequence_words(adjectives)}")

        # Print object attributes (variable number)
        for a, v in attributes.items():
            description = sequence_words(v)
            if description != "":
                line_out.append(f"{rail}= Its {a.lower()} is {str(description)}")

        # Print object traits (one of each)
        for a, v in traits.items():
            if a not in treasure_core.NoDescribe:
                line_out.append(f"{rail}- Its {a.lower()} is {sequence_words(v)}")

        # Print object embellishments (one of each, as passive verbs)
        for a, v in additional.items():
            line_out.append(f"{rail}* It {v.as_pverb()}")

    if recursive:
        for i, v in enumerate(components.items()):
            prefix_first, prefix_rest = ("\\_", "  ") if i == len(components) - 1 else ("|_", "| ")
            ret = item_description(v[1], top=False)

            line_return = [prefix_first + "[{}] Its {} is {}".format(i, v[0].lower(), ret.pop(0))]
            line_return += [prefix_rest + line for line in ret]
            line_out += line_return

    return line_out


def describe_item(item):
    line_in = item_description(item)
    line_out = "\n".join(line_in)
    print(line_out)
