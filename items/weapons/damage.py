"""
Weapon Parts that contribute damage to the weapon. Blades, heads, points, spikes...Anything that can be used to kill.
"""
from items import materials

# from treasure_core import TreasureObject, form_out
from .structure import WPart


class Damager(WPart):
    size = 10
    type_damage = {  # Coefficients of each damage type done by this component
    }

    # How much damage does it do? (This will be greatly multiplied later)
    base_damage = 10
    # How fast can it be used?
    base_speed = 10

    Effectiveness = 4  # How much better the "good" damages are than the "bad" damages
    DamageTypesGood = []  # List of damage types that this component is good for
    DamageTypesBad = []  # List of damage types that this component is bad for
    # 0: Crush, 1: Pierce, 2: Slice

    traits = {"Material": (materials.Metal.weapons, [100, 90, 50, 1])}
    base_durability = 5
    TreasureType = "Weapon Component"


class Blade(Damager):
    """A long flat plane with sharp edges"""

    size = 8
    type_damage = {  # Coefficients of each damage type done by this component
        "Crush": {"Density": 1, "Hardness": 0.5, "Flexibility": -0.2},
        "Pierce": {"Density": 0.3, "Hardness": 1, "Flexibility": 0.5},
        "Slice": {"Density": 0.2, "Hardness": 1, "Flexibility": 1},
    }

    base_damage = 10
    base_speed = 10

    Effectiveness = 4
    DamageTypesGood = [2]
    DamageTypesBad = []

    base_durability = 4
    TreasureType = "typical blade"


class BladeBig(Damager):
    """A long flat plane with sharp edges"""

    size = 14
    base_damage = 12
    base_speed = 6

    Effectiveness = 5
    DamageTypesGood = [2]
    DamageTypesBad = [1]

    base_durability = 4
    TreasureType = "great blade"


class Sphere(Damager):
    """A basic and smooth orb"""

    size = 2
    type_damage = {  # Coefficients of each damage type done by this component
        "Crush": {"Density": 1.4, "Hardness": 0.2, "Flexibility": 0}
    }
    Effectiveness = 2
    DamageTypesGood = [0]
    TreasureType = "simple orb"


class HeadClub(Damager):
    """A smooth heavy block or cylinder"""

    size = 6
    type_damage = {  # Coefficients of each damage type done by this component
        "Crush": {"Density": 2.4, "Hardness": 0.1, "Flexibility": 0.2}
    }
    Effectiveness = 8
    DamageTypesGood = [0]
    TreasureType = "club head"


class HeadMace(Damager):
    """A heavy cylinder, with flanges or blades attached"""

    size = 6
    type_damage = {  # Coefficients of each damage type done by this component
        "Crush": {"Density": 2.1, "Hardness": 0.1, "Flexibility": 0.2},
        "Slice": {"Density": 0, "Hardness": 0.3, "Flexibility": 0.1},
    }
    Effectiveness = 6
    DamageTypesGood = [0]
    TreasureType = "flanged head"


class HeadStar(Damager):
    """A heavy mass, with spikes attached"""

    size = 6
    type_damage = {  # Coefficients of each damage type done by this component
        "Crush": {"Density": 2.1, "Hardness": 0.1, "Flexibility": 0.2},
        "Pierce": {"Density": 0, "Hardness": 0.3, "Flexibility": 0.1},
    }
    Effectiveness = 8
    DamageTypesGood = [0]
    TreasureType = "spiked head"
