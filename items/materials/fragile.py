from .base_material import Material


class Fragile(Material):
    Value = 80
    Rarity = 60
    Density = 80
    Hardness = 50
    Toughness = 10
    Flexibility = 30
    # Damage FX; Adjectives applied when item is damaged
    dmg_FX = {
        "phys": ["scratched", "chipped", "cracked", "broken"],
        "burn": ["singed", "charred", "melted"],
    }

    clear = []
    opaque = []


class Glass(Fragile):
    adj = "Glass"


class Crystal(Fragile):
    Hardness = 30
    adj = "Crystal"


class Porcelain(Fragile):
    Hardness = 20
    Toughness = 5
    adj = "Porcelain"


class Ceramic(Fragile):
    Toughness = 20
    adj = "Ceramic"


class Obsidian(Fragile):
    Hardness = 200
    adj = "Obsidian"


Fragile.all = [Glass, Crystal, Porcelain, Ceramic, Obsidian]
Fragile.clear = [Glass, Crystal]
Fragile.opaque = [Porcelain, Ceramic, Obsidian]
