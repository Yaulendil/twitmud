
def title_item(item):
    return item.strself()


def item_description(item, top=True):
    line_out = []

    traits = item.dictTrait
    attributes = item.dictAttr
    components = item.dictComp
    additional = item.dictAdd

    line_out.append(title_item(item))

    for i, v in enumerate(components.items()):
        prefix_first, prefix_rest = ("\\_", "  ") if i == len(components) - 1 else ("|_", "| ")
        ret = item_description(v[1], False)

        line_return = [prefix_first + ret.pop(0)]
        line_return += [prefix_rest + line for line in ret]

        line_out += line_return

    return line_out


def describe_item(item):
    line_in = item_description(item)
    line_out = "\n".join(line_in)
    print(line_out)
