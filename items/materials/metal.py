from .base_material import Material


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
    adj = "Metal"


class Iron(Metal):
    Value = 100
    Rarity = 100
    Density = 100
    Hardness = 100
    Toughness = 100
    Flexibility = 100
    adj = "Iron"


class Steel(Metal):
    Value = 150
    Rarity = 140
    Density = 130
    Hardness = 200
    Toughness = 200
    Flexibility = 100
    adj = "Steel"


class Brass(Metal):
    Value = 180
    Rarity = 120
    Density = 120
    Hardness = 60
    Toughness = 130
    Flexibility = 50
    adj = "Brass"


class Bronze(Metal):
    Value = 80
    Rarity = 120
    Density = 115
    Hardness = 95
    Toughness = 90
    Flexibility = 120
    adj = "Brazen"


class Copper(Metal):
    Value = 70
    Rarity = 80
    Density = 110
    Hardness = 80
    Toughness = 75
    Flexibility = 130
    adj = "Copper"


class Silver(Metal):
    Value = 20000
    Rarity = 1000
    Density = 130
    Hardness = 50
    Toughness = 85
    Flexibility = 100
    adj = "Silver"


class Gold(Metal):
    Value = 30000
    Rarity = 10000
    Density = 250
    Hardness = 30
    Toughness = 80
    Flexibility = 100
    adj = "Golden"


class Mithril(Metal):
    Value = 200000
    Rarity = 20000
    Density = 25
    Hardness = 400
    Toughness = 200
    Flexibility = 150
    adj = "Mithril"


class Adamantium(Metal):
    Value = 200000
    Rarity = 20000
    Density = 300
    Hardness = 70
    Toughness = 220
    Flexibility = 20
    adj = "Adamantine"


Metal.all = [Iron, Steel, Copper, Bronze, Silver, Gold, Mithril, Adamantium]
Metal.weapons = [[Iron, Copper, Bronze], [Steel], [Silver, Gold], [Mithril, Adamantium]]
Metal.decor = [[Copper, Bronze, Brass], [Silver], [Gold]]
Metal.structure = [[Copper, Bronze, Brass], [Iron], [Steel]]
