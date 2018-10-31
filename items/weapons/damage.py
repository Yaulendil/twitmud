"""
Weapon Parts that contribute damage to the weapon. Blades, heads, points, spikes...Anything that can be used to kill.
"""
from items import materials

# from treasure_core import TreasureObject, form_out
from .structure import WPart


class Damager(WPart):
    size = 10
    type_damage = {  # Coefficients of each damage type done by this component
        "Crush": {"Density": 1, "Hardness": 0.5, "Flexibility": -0.2},
        "Pierce": {"Density": 0.3, "Hardness": 1, "Flexibility": 0.5},
        "Slice": {"Density": 0.2, "Hardness": 1, "Flexibility": 1},
    }

    # How much damage does it do? (This will be greatly multiplied later)
    base_damage = 10
    # How fast can it be used?
    base_speed = 10

    Effectiveness = 4  # How much better the "good" damages are than the "bad" damages
    DamageTypesGood = []  # List of damage types that this component is good for
    DamageTypesBad = []  # List of damage types that this component is bad for
    # 0: Crush, 1: Pierce, 2: Slice

    traits = {"Material": materials.Metal.weapons}
    base_durability = 5
    TreasureType = "Weapon Component"


class Blade(Damager):
    size = 8
    base_damage = 10
    base_speed = 10

    Effectiveness = 4
    DamageTypesGood = [2]
    DamageTypesBad = [0]

    traits = {"Material": materials.Metal.weapons}
    base_durability = 4
    TreasureType = "typical blade"


class Sphere(Damager):
    size = 2
    """A basic and smooth orb"""
    type_damage = {  # Coefficients of each damage type done by this component
        "Crush": {"Density": 1, "Hardness": 0.8, "Flexibility": 0},
        "Pierce": {"Density": 0, "Hardness": 0, "Flexibility": 0},
        "Slice": {"Density": 0, "Hardness": 0, "Flexibility": 0},
    }
    TreasureType = "simple orb"
