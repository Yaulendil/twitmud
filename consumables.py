from treasure_core import TreasureObject


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
            "yellow",
            "golden",
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
            "silvery",
            "chocolate",
            "woody",
            "mocha",
            "colorless",
        ],
        "Visual": ["opaque", "cloudy", "clear", "murky"],
        "Texture": ["thick", "thin", "lumpy", "smooth", "chunky", "pulpy"],
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


class fluidWater(Fluid):
    attrs = {}
    traits = {
        "Color": ["colorless"],
        "Visual": (["cloudy", "clear", "murky"], [0.3, 0.6, 0.1]),
    }
    # "Texture":["thick","thin","lumpy",
    # "smooth","chunky","pulpy"]}
    # TreasureType = "water"


class Bottle(TreasureObject):
    components = {"Content": Fluid}
    traits = {
        "Material": ["glass", "crystal", "plastic"],
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


class Potion(TreasureObject):
    components = {"Bottle": Bottle}
    TreasureType = "potion"


class bottleWater(Bottle):
    components = {"Content": fluidWater}
    TreasureType = "water bottle"
