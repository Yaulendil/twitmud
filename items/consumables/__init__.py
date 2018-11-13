from items.treasure_core import TreasureObject
from items import materials, decor
from selection import choose_from
from . import fluid


Labels = [
    [None],
    ["Beer", "Wine", "Water", "Whiskey"],
    ["Healing", "Death", "Poison"],
    ["XXX", "???", "!!!"],
]


def wine_label():
    brands = ["O'Malley's", "Steady Hand McDuff's", "Undertaker", "Trés Comas"]
    names = ["Finest", "Special Reserve", "Dry", "VSOP"]
    years = range(1911, 2003)
    return " ".join([choose_from(brands)[0], choose_from(names)[0], str(choose_from(years)[0])])


############
# Closures #
############


class Stopper(TreasureObject):
    materials = [materials.Cork] + materials.Fragile.clear

    image = ["   ▃   "]

    additions = [
        ([None, decor.GemEncrust], [10, 1]),
        ([None, decor.MetalFoil], [10, 1]),
    ]
    TreasureType = "stopper"
    class_flags = ["CAN_REMOVE"]
    size = 1


class CrownCap(TreasureObject):
    materials = materials.Metal.decor

    image = ["   ▂   "]

    additions = [
        ([None, decor.MetalInlay], [10, 1]),
        ([None, decor.MetalFoil], [10, 1]),
    ]
    TreasureType = "crown cap"
    class_flags = ["CAN_REMOVE", "CANNOT_ATTACH"]
    size = 1


class ScrewCap(TreasureObject):
    materials = materials.Metal.decor

    image = ["   ▂   "]

    additions = [
        ([None, decor.MetalPlating], [10, 1]),
        ([None, decor.MetalFoil], [10, 1]),
    ]
    TreasureType = "screw cap"
    class_flags = ["CAN_REMOVE"]
    size = 1


class FlipTop(TreasureObject):
    materials = materials.Metal.decor

    image = ["  ╭┰╮  ", "  ╞▅╡  "]

    TreasureType = "flip top"
    size = 1


###########
# Vessels #
###########


class Bottle(TreasureObject):
    materials = materials.Fragile.all

    image = ["   █   ", " ▗▟█▙▖ ", " █████ ", " ▒▒▒▒▒ ", " ▜███▛ "]

    traits = {
        "Fullness": range(20, 100, 5),
        "Shape": [
            "spherical",
            "tetrahedric",
            "cubic",
            "octohedric",
            "decahedric",
            "dodecahedric",
            "icosahedric",
        ],
    }
    additions = [
        ([None, decor.Basket], [6, 1]),
    ]
    TreasureType = "bottle"
    size = 3


class Flask(Bottle):
    materials = materials.Metal.decor + materials.Fragile.opaque

    image = ["  ▗█▖  ", " ▟███▙ ", " ▒▒▒▒▒ ", " ▜███▛ "]

    TreasureType = "flask"


class Vial(Bottle):
    materials = materials.Fragile.clear

    image = ["   █   ", " ▗███▖ ", " ▒▒▒▒▒ ", " ▜███▛ "]

    TreasureType = "vial"


##################
# Complete items #
##################


class BottledLiquid(TreasureObject):
    components = {
        "Closure": [Stopper, CrownCap, ScrewCap, FlipTop],
        "Vessel": [Bottle, Flask, Vial],
    }

    TreasureType = "container"
    primary = "Vessel"

    def __init__(self, *arg, content=None, label=None, **kw):
        super().__init__(*arg, **kw)
        self.dictComp["Content"] = content
        if label is True:
            label = choose_from(Labels)[0]
        if label:
            self.decor.append(decor.Label(text=label))


def bottle_water():
    return BottledLiquid(content=fluid.Water(), label="Water")


def bottle_wine():
    return BottledLiquid(content=fluid.Wine(), label=wine_label())


def bottle_potion():
    return BottledLiquid(content=fluid.Potion(), label=True)
