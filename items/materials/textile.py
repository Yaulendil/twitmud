from .base_material import Material


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
    adj = "Textile"


class Leather(Textile):
    Toughness = 60
    adj = "Leather"


class Silk(Textile):
    Toughness = 15
    adj = "Silken"


class Cotton(Textile):
    adj = "Cotton"


class Linen(Textile):
    adj = "Linen"


class Canvas(Textile):
    adj = "Canvas"


class Wool(Textile):
    adj = "Woollen"


Textile.all = [Leather, Silk, Cotton, Linen, Canvas, Wool]
Textile.common = [Leather, Canvas, Cotton, Linen]
Textile.fine = [Silk, Wool]
