from items.treasure_core import TreasureObject
from items import materials, decor

from . import fluid


Labels = [
    [None],
    ["Beer", "Wine", "Water", "Whiskey"],
    ["Healing", "Death", "Poison"],
    ["XXX", "???", "!!!"],
]


############
# Closures #
############


class Stopper(TreasureObject):
    materials = materials.Wood.all

    image = ["   ▃   "]

    additions = [
        ([None, decor.GemEncrust], [10, 1]),
        ([None, decor.MetalFoil], [10, 1]),
    ]
    TreasureType = "stopper"
    size = 1


class CrownCap(TreasureObject):
    materials = materials.Metal.decor

    image = ["   ▂   "]

    additions = [
        ([None, decor.MetalInlay], [10, 1]),
        ([None, decor.MetalFoil], [10, 1]),
    ]
    TreasureType = "crown cap"
    size = 1


class ScrewCap(TreasureObject):
    materials = materials.Metal.decor

    image = ["   ▂   "]

    additions = [
        ([None, decor.MetalPlating], [10, 1]),
        ([None, decor.MetalFoil], [10, 1]),
    ]
    TreasureType = "screw cap"
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


class Potion(TreasureObject):
    components = {
        "Closure": [Stopper, CrownCap, ScrewCap, FlipTop],
        "Vessel": [Bottle, Flask, Vial],
    }

    TreasureType = "container"
    primary = "Vessel"

    def __init__(self, *arg, content=None, **kw):
        super().__init__(*arg, **kw)
        self.dictComp["Content"] = content
