from .base_material import Material


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


class Cork(Wood):
    Density = 2
    Hardness = 10
    Toughness = 10
    __adj__ = "Cork"


Wood.all = [Oak, Elm, Maple, Redwood, Willow, Mahogany, Spruce, Cork]
Wood.structure = [Oak, Spruce, Maple, Willow]
