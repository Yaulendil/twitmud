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
    adj = "Wooden"


class Oak(Wood):
    adj = "Oaken"


class Elm(Wood):
    adj = "Elm"


class Maple(Wood):
    adj = "Maple"


class Redwood(Wood):
    adj = "Redwood"


class Willow(Wood):
    adj = "Willow"


class Mahogany(Wood):
    adj = "Mahogany"


class Spruce(Wood):
    adj = "Spruce"


class Cork(Wood):
    Density = 2
    Hardness = 10
    Toughness = 10
    adj = "Cork"


Wood.all = [Oak, Elm, Maple, Redwood, Willow, Mahogany, Spruce, Cork]
Wood.structure = [Oak, Spruce, Maple, Willow]
