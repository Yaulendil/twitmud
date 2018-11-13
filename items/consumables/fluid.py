from items.treasure_core import TreasureObject


class Fluid(TreasureObject):
    attrs = {}
    traits = {
        "Color": ["colorless"],
        "Visual": (["cloudy", "clear", "murky"], [3, 6, 1]),
    }
    TreasureType = "unknown fluid"
    BaseType = "fluid"


class Water(Fluid):
    pass


class Wine(Fluid):
    attrs = {"Effect": (0, 1, ["sparkling", "bubbling"])}
    traits = {
        "Color": [["tawny", "rose"], ["ruby", "red"], ["golden"]],
        "Visual": ["opaque", "clear"],
    }


class Potion(Fluid):
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
            "rose",
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
            "tarry",
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
