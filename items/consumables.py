from items.treasure_core import TreasureObject
from items import materials


class Fluid(TreasureObject):
    attrs = {
        "Effect": (
            0,
            2,
            [
                "smoking",
                "steaming",
                "sparkling",
                "bubbling",
                "glowing",
                "humming",
                "flaming",
                "boiling",
                "swirling",
                "popping",
            ],
        )
    }
    traits = {
        "Color": [
            "red",
            "ruby",
            "orange",
            "topaz",
            "yellow",
            "golden",
            "sunshine",
            "green",
            "emerald",
            "blue",
            "cyan",
            "sky",
            "turquoise",
            "indigo",
            "sapphire",
            "midnight",
            "purple",
            "violet",
            "amethyst",
            "black",
            "tar",
            "pitch",
            "coal",
            "white",
            "milky",
            "grey",
            "silvery",
            "chocolate",
            "woody",
            "mocha",
            "colorless",
        ],
        "Visual": ["opaque", "cloudy", "clear", "murky"],
        "Texture": ["thick", "thin", "lumpy", "smooth", "chunky", "pulpy"],
        # "Effect": ["strength", "weakness", "health", "poison", "fire", "speed", "slowness", "darkvision", "blindness"],
    }
    TreasureType = "unknown fluid"
    BaseType = "fluid"

    # def desc(self, solo=True, pad=""):
    # o = "{v}{c} fluid"
    ##if not solo:
    ##return o.format(v = " "+self.attrDict["Visual"], c = " "+self.attrDict["Color"])
    # l1 = [self.attrDict["Texture"]] + self.attrDict["Effect"]
    # s = SequenceWords(l1)
    # if s != "":
    # o += " is " + s
    # o = "The"+o+"."
    # return o.format(v = " "+self.attrDict["Visual"], c = " "+self.attrDict["Color"])


class FluidWater(Fluid):
    attrs = {}
    traits = {
        "Color": ["colorless"],
        "Visual": (["cloudy", "clear", "murky"], [0.3, 0.6, 0.1]),
    }
    # "Texture":["thick","thin","lumpy",
    # "smooth","chunky","pulpy"]}
    # TreasureType = "water"


class Bottle(TreasureObject):
    materials = materials.Metal.decor
    components = {"Content": Fluid,
                  "Other content": Fluid}
    traits = {
        "Fullness": range(20, 100, 5),
        # "Vessel":["bottle","flask","vial"],
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

    # def desc(self, solo=True, pad=""):
    # o = "The {Shape} {Material} {Vessel} is {Fullness}% full.".format(**self.attrDict)
    # for sub in self.compDict:
    # o += "\n    " + self.compDict[sub].describe().replace("fluid","fluid within")
    # return o

    # def describe(self, solo=True, pad=""):
    # o = self.desc(solo,pad)
    # return o


class Flask(Bottle):
    TreasureType = "flask"


class Vial(Bottle):
    TreasureType = "vial"


class Potion(TreasureObject):
    components = {"Bottle": [Bottle, Flask, Vial]}
    TreasureType = "potion"


class BottleWater(Bottle):
    components = {"Content": FluidWater}
    TreasureType = "water bottle"
