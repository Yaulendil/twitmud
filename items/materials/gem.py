from .base_material import Material


class Gemstone(Material):
    Value = 200
    Rarity = 1000
    Density = 10
    Hardness = 300
    Toughness = 10
    Flexibility = 20
    # Damage FX; Adjectives applied when item is damaged
    dmg_FX = {
        "phys": ["scratched", "cracked", "crushed"],
        # "burn": ["singed", "charred", "melted"],
    }
    __adj__ = "Gem"


class Ruby(Gemstone):
    Value = 300


class Topaz(Gemstone):
    Value = 175


class Emerald(Gemstone):
    Value = 250


class Turquoise(Gemstone):
    Value = 200


class Sapphire(Gemstone):
    Value = 275


class Amethyst(Gemstone):
    Value = 225


class Onyx(Gemstone):
    Value = 600


class Diamond(Gemstone):
    Value = 500


class Quartz(Gemstone):
    Value = 150


Gemstone.all = [Ruby, Topaz, Emerald, Turquoise, Sapphire, Amethyst, Onyx, Diamond, Quartz]
Gemstone.common = [Topaz, Turquoise, Amethyst, Quartz]
Gemstone.fine = [Ruby, Emerald, Sapphire]
Gemstone.rare = [Onyx, Diamond]

