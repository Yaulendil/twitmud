"""
MATERIALS provide the BASE VALUE of an object, as well as its physical stats.
An object can be made from any material which has all the required stats for the object type.
"""

METAL = {
    "Iron": {  # "Standard" metal, quite balanced
        "Value": 10,  # Monetary worth of the material
        "Density": 10,  # How much mass is in a given volume; Weapon weight
        "Hardness": 10,  # How well a weapon maintains shape; Aids sharpness
        "Toughness": 10,  # Difficulty to permanently deform; Durability
        "Flexibility": 10,  # Ability to temporarily deform
    },
    "Steel": {  # Alloyed iron, generally better but more brittle
        "Value": 14,
        "Density": 10,
        "Hardness": 12,
        "Toughness": 10,
        "Flexibility": 10,
    },
    "Brass": {  # An aesthetically pleasant alloy; Not particularly exceptional
        "Value": 12,
        "Density": 12,
        "Hardness": 14,
        "Toughness": 14,
        "Flexibility": 10,
    },
    "Bronze": {  # A weapons-grade alloy of cheaper metals
        "Value": 8,
        "Density": 9,
        "Hardness": 9,
        "Toughness": 8,
        "Flexibility": 12,
    },
    "Copper": {  # A cheap metal, easily outclassed
        "Value": 6,
        "Density": 8,
        "Hardness": 7,
        "Toughness": 10,
        "Flexibility": 11,
    },
    "Silver": {  # Precious metal, soft but rather heavy
        "Value": 16,
        "Density": 15,
        "Hardness": 7,
        "Toughness": 10,
        "Flexibility": 8,
    },
    "Gold": {  # Very precious metal, quite soft but very heavy
        "Value": 18,
        "Density": 18,
        "Hardness": 5,
        "Toughness": 10,
        "Flexibility": 8,
    },
    "Mithril": {  # Legendary metal, unnaturally light and sharp
        "Value": 24,
        "Density": 6,
        "Hardness": 12,
        "Toughness": 10,
        "Flexibility": 14,
    },
    "Adamantium": {  # Legendary metal, unnaturally hard and heavy
        "Value": 24,
        "Density": 22,
        "Hardness": 10,
        "Toughness": 10,
        "Flexibility": 10,
    },
}

MetalDist = {
    "Iron": 0.25,  # Probability for each material to be selected; Must sum to 1
    "Steel": 0.20,
    "Brass": 0.10,
    "Bronze": 0.20,
    "Copper": 0.10,
    "Silver": 0.05,
    "Gold": 0.05,
    "Mithril": 0.02,
    "Adamantium": 0.03,
}

WOOD = {
    "Oak": {"Value": 3, "Toughness": 6},
    "Pine": {"Value": 4, "Toughness": 5},
    "Mahogany": {"Value": 8, "Toughness": 8},
    "Balsa": {"Value": 2, "Toughness": 3},
}

GEMSTONE = {}

TEXTILE = {
    "Leather": {"Value": 3, "Toughness": 3},
    "Silk": {"Value": 3, "Toughness": 1},
    "Cotton": {"Value": 3, "Toughness": 1},
    "Wool": {"Value": 3, "Toughness": 2},
}

GLASS = {"Glass": {"Value": 3, "Toughness": 1}, "Crystal": {"Value": 7, "Toughness": 1}}


class Material:
    Value = 100
    Rarity = 100
    Density = 100
    Hardness = 100
    Toughness = 100
    Flexibility = 100
    # Damage FX; Adjectives applied when item is damaged
    dmg_FX = {
        "phys": ["damaged", "broken", "destroyed"],
        "burn": ["singed", "charred", "melted"],
    }
    # Aesthetic FX; Adjectives applied when item is cold, bloody, etc
    aes_FX = {
        "cold": ["frosted", "frozen"],
        "blood": [
            "blood-speckled",
            "blood-spattered",
            "bloody",
            "bloodsoaked",
            "sanguinated",
        ],
    }
    __adj__ = "Physical"

    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return self.__name__.lower()


class Metal(Material):
    # Damage FX; Adjectives applied when item is damaged
    dmg_FX = {
        "phys": ["dented", "chipped", "cracked", "broken"],
        # "burn": ["singed", "charred", "melted"],
    }
    # Aesthetic FX; Adjectives applied when item is cold, bloody, etc
    aes_FX = {
        # "cold": ["frosted", "frozen"],
        "blood": [
            "blood-speckled",
            "blood-spattered",
            "bloody",
            "bloodsoaked",
            "sanguinated",
        ],
    }
    __adj__ = "Metal"


class Iron(Metal):
    Value = 100
    Rarity = 100
    Density = 100
    Hardness = 100
    Toughness = 100
    Flexibility = 100
    __adj__ = "Iron"


class Steel(Metal):
    Value = 150
    Rarity = 140
    Density = 130
    Hardness = 200
    Toughness = 200
    Flexibility = 100
    __adj__ = "Steel"


class Brass(Metal):
    Value = 180
    Rarity = 120
    Density = 120
    Hardness = 60
    Toughness = 130
    Flexibility = 50
    __adj__ = "Brass"


class Bronze(Metal):
    Value = 80
    Rarity = 120
    Density = 115
    Hardness = 100
    Toughness = 90
    Flexibility = 100
    __adj__ = "Brazen"


class Copper(Metal):
    Value = 70
    Rarity = 80
    Density = 110
    Hardness = 100
    Toughness = 75
    Flexibility = 100
    __adj__ = "Copper"


class Silver(Metal):
    Value = 20000
    Rarity = 1000
    Density = 130
    Hardness = 50
    Toughness = 85
    Flexibility = 100
    __adj__ = "Silver"


class Gold(Metal):
    Value = 30000
    Rarity = 10000
    Density = 250
    Hardness = 30
    Toughness = 80
    Flexibility = 100
    __adj__ = "Golden"


class Mithril(Metal):
    Value = 200000
    Rarity = 20000
    Density = 25
    Hardness = 400
    Toughness = 200
    Flexibility = 150
    __adj__ = "Mithril"


class Adamantium(Metal):
    Value = 200000
    Rarity = 20000
    Density = 300
    Hardness = 70
    Toughness = 220
    Flexibility = 20
    __adj__ = "Adamantine"


class Wood(Material):
    Value = 20
    Rarity = 10
    Density = 10
    Hardness = 30
    Toughness = 30
    Flexibility = 200
    # Damage FX; Adjectives applied when item is damaged
    dmg_FX = {
        "phys": ["cracked", "splintering", "broken"],
        "burn": ["singed", "charred", "burnt"],
    }
    # Aesthetic FX; Adjectives applied when item is cold, bloody, etc
    aes_FX = {
        # "cold": ["frosted", "frozen"],
        "blood": [
            "blood-speckled",
            "blood-spattered",
            "bloody",
            "bloodsoaked",
            "sanguinated",
        ],
    }
    __adj__ = "Wooden"


class Oak(Wood):
    __adj__ = "Oaken"


class Elm(Wood):
    __adj__ = "Elm"


class Maple(Wood):
    __adj__ = "Maple"


class Redwood(Wood):
    __adj__ = "Redwood"


class Willow(Wood):
    __adj__ = "Willow"


class Mahogany(Wood):
    __adj__ = "Mahogany"


class Spruce(Wood):
    __adj__ = "Spruce"


class Textile(Material):
    Value = 40
    Rarity = 10
    Density = 10
    Hardness = 30
    Toughness = 30
    Flexibility = 600
    # Damage FX; Adjectives applied when item is damaged
    dmg_FX = {
        "phys": ["worn", "frayed", "torn", "ripped", "shredded"],
        "burn": ["singed", "charred", "burnt"],
    }
    # Aesthetic FX; Adjectives applied when item is cold, bloody, etc
    aes_FX = {
        # "cold": ["frosted", "frozen"],
        "blood": [
            "blood-speckled",
            "blood-spattered",
            "bloody",
            "bloodsoaked",
            "sanguinated",
        ],
    }
    __adj__ = "Textile"


class Leather(Textile):
    __adj__ = "Leather"


class Silk(Textile):
    __adj__ = "Silken"


class Cotton(Textile):
    __adj__ = "Cotton"


class Canvas(Textile):
    __adj__ = "Canvas"


class Wool(Textile):
    __adj__ = "Woollen"


class Gemstone(Material):
    Value = 200
    Rarity = 1000
    Density = 10
    Hardness = 300
    Toughness = 10
    Flexibility = 20
    __adj__ = "Crystalline"


Metal.weapons = [[Iron, Copper, Bronze], [Steel], [Silver, Gold], [Mithril, Adamantium]]
Metal.decor = [[Copper, Bronze, Brass], [Silver], [Gold]]
Metal.structure = [[Copper, Bronze, Brass], [Iron], [Steel]]

Wood.all = [Oak, Elm, Maple, Redwood, Willow, Mahogany, Spruce]
Wood.structure = [Oak, Spruce, Maple]

Textile.all = [Leather, Silk, Cotton, Canvas, Wool]
Textile.common = [Leather, Canvas]
Textile.fine = [Silk, Wool]
