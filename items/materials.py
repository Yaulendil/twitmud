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

    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return self.__name__.lower()


class Metal(Material):
    pass


class Iron(Metal):
    Value = 100
    Rarity = 100
    Density = 100
    Hardness = 100
    Toughness = 100
    Flexibility = 100


class Steel(Metal):
    Value = 100
    Rarity = 100
    Density = 130
    Hardness = 100
    Toughness = 200
    Flexibility = 100


class Brass(Metal):
    Value = 100
    Rarity = 100
    Density = 100
    Hardness = 100
    Toughness = 100
    Flexibility = 100


class Bronze(Metal):
    Value = 100
    Rarity = 100
    Density = 100
    Hardness = 100
    Toughness = 90
    Flexibility = 100


class Copper(Metal):
    Value = 100
    Rarity = 100
    Density = 110
    Hardness = 100
    Toughness = 75
    Flexibility = 100


class Silver(Metal):
    Value = 20000
    Rarity = 1000
    Density = 130
    Hardness = 50
    Toughness = 85
    Flexibility = 100


class Gold(Metal):
    Value = 30000
    Rarity = 10000
    Density = 250
    Hardness = 30
    Toughness = 80
    Flexibility = 100


class Mithril(Metal):
    Value = 200000
    Rarity = 20000
    Density = 25
    Hardness = 400
    Toughness = 200
    Flexibility = 150


class Adamantium(Metal):
    Value = 200000
    Rarity = 20000
    Density = 300
    Hardness = 70
    Toughness = 220
    Flexibility = 20


Metal.weapons = [[Iron, Copper, Bronze],
                 [Steel],
                 [Silver, Gold],
                 [Mithril, Adamantium]]

Metal.decor = [[Copper, Bronze, Brass],
               [Silver],
               [Gold]]

Metal.structure = [[Copper, Bronze, Brass],
                   [Iron], [Steel]]


class Wood(Material):
    Value = 20
    Rarity = 10
    Density = 10
    Hardness = 30
    Toughness = 30
    Flexibility = 200


class Textile(Material):
    pass


class Gemstone(Material):
    pass
