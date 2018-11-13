from .base_material import Material


class Fragile(Material):
    Value = 100
    Rarity = 100
    Density = 100
    Hardness = 100
    Toughness = 100
    Flexibility = 100
    # Damage FX; Adjectives applied when item is damaged
    dmg_FX = {
        "phys": ["scratched", "chipped", "cracked", "broken"],
        "burn": ["singed", "charred", "melted"],
    }

    clear = []
    opaque = []


class Glass(Fragile):
    __adj__ = "Glass"


class Crystal(Fragile):
    __adj__ = "Crystal"


class Porcelain(Fragile):
    __adj__ = "Porcelain"


class Ceramic(Fragile):
    __adj__ = "Ceramic"


class Obsidian(Fragile):
    __adj__ = "Obsidian"


Fragile.all = [Glass, Crystal, Porcelain, Ceramic, Obsidian]
Fragile.clear = [Glass, Crystal]
Fragile.opaque = [Porcelain, Ceramic, Obsidian]
