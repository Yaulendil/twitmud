import random
from numpy import add as npadd

from treasure_core import TreasureObject, form_out
from consumables import bottleWater, Potion, Bottle
from materials import METAL, WOOD, GEMSTONE, GLASS, TEXTILE


class Weapon(TreasureObject):
    TreasureType = "Generic Weapon"

    def __init__(self, *args, **kwargs):
        self.Damage = 0  # WEAPONS deal damage determined by their components
        super().__init__(self, *args, **kwargs)
        self.calcDamage()

    def calcSize(self):
        S = 1
        return S

    def calcDamage(self):
        D = [0, 0, 0]
        for comp in self.dictComp:
            D = npadd(D, self.dictComp[comp].damageRating(True))
        return list(D)

    def describe(self, solo=True, pad="", full=False):
        o = ""
        if solo:
            o += pad + f"'This is {self}.'"
        D = self.calcDamage()
        o += form_out(
            f"It does {'/'.join([str(i) for i in D])} C/P/S damage for {sum(D)} ideal-total.",
            pad,
        )
        o += super().describe(False, pad, full)
        return o


def DB(*args):
    print(*args, sep=" // ")
    pass


class wPart(TreasureObject):
    traits = {"Material": METAL}
    TreasureType = "Weapon Component"
    baseDurability = 5

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        # Base values; Multiplied later
        self.Size = (
            1
        )  # Approximate volume occupied by the component; Affects reach and weight
        self.HP = (
            self.baseDurability * self.MatStat["Toughness"]
        )  # "Health" of a part determines when it breaks and what its damage adjective is

    @property
    def MatStat(self):
        test = self.traits["Material"]
        if type(test) == tuple:
            test = test[0]
        test = test[self.dictTrait["Material"]]  # Get the base stat table
        return test
        # noinspection PyUnreachableCode
        """
                {"Value":10, # Monetary worth of the material
                 "Density":10, # How much mass is in a given volume; Weapon weight
                 "Hardness":10, # How well a weapon maintains shape; Aids sharpness
                 "Toughness":10, # Difficulty to permanently deform; Durability
                 "Flexibility":10}, # Ability to temporarily deform
                """

    def damageRating(
        self, split=True
    ):  # Amount of damage contributed by this component
        D = []
        try:
            dBase = self.MatStat  # Damage bases
            dScale = self.mapDamage  # Damage scale factors
            # DB(self,dBase,dScale)
            for (
                n
            ) in dScale:  # Do the following for EACH STAT and then add it to the list
                # DB(n,dScale[n],D)
                D.append(
                    float(
                        dScale[n]  # wp.mapDamage["Density"] (0.5)
                        * dBase[n]  # MULTIPLIED by dBase["Density"] (10)
                        * self.baseDamage
                    )
                )  # AND by base damage of the component class
        except Exception as e:
            D = [0, 0, 0]
            # DB(e)
        for i in range(len(D)):
            try:  # D[i] should be a matching damage type...
                assert i in self.DamageTypes
            except:  # ...Otherwise, make it relatively bad
                D[i] /= 4
        return [round(i, 2) for i in D]

    def describe(self, solo=True, pad="", full=False):
        o = super().describe(solo, pad, full)
        D = self.damageRating()
        if sum(D) > 0:
            o += form_out(f"It contributes {D} C/P/S damage.", pad, True)
        return o


# Damage-dealing Parts #

# Sliceing weapons; Longswords, daggers, etc
class wp_Slice_1(wPart):
    mapDamage = {  # How much each material statistic impacts the damage done by this component
        "Density": 0.5,
        "Hardness": 1,
        "Flexibility": 2,
    }
    DamageTypes = [2]  # List of damage types that this component is good for
    baseDamage = 10
    baseSpeed = 14
    TreasureType = "single-edged blade"
    baseDurability = 5


class wp_Slice_1_small(wp_Slice_1):
    baseDamage = 6
    baseSpeed = 20
    TreasureType = "short single-edged blade"


class wp_Slice_2(wPart):
    mapDamage = {"Density": 0.5, "Hardness": 1, "Flexibility": 2}
    DamageTypes = [2]
    baseDamage = 12
    baseSpeed = 12
    TreasureType = "double-edged blade"
    baseDurability = 5


class wp_Slice_2_small(wp_Slice_2):
    baseDamage = 6
    baseSpeed = 20
    TreasureType = "short double-edged blade"


# Thrusting weapons; Rapiers, spears, etc
class wp_Thrust(wPart):
    mapDamage = {"Density": 1, "Hardness": 2, "Flexibility": 0.5}
    DamageTypes = [1]
    baseDamage = 12
    baseSpeed = 16
    TreasureType = "tip"
    baseDurability = 6


# Thrusting weapons; Rapiers, spears, etc
class wp_ThrustBlade(wPart):
    mapDamage = {"Density": 1, "Hardness": 2, "Flexibility": 0.5}
    DamageTypes = [1]
    baseDamage = 12
    baseSpeed = 16
    TreasureType = "edgeless blade"
    baseDurability = 6


# Blunt weapons; Maces, hammers, etc
class wp_Crush(wPart):
    mapDamage = {"Density": 2, "Hardness": 1, "Flexibility": 0.5}
    DamageTypes = [0]
    baseDamage = 12
    baseSpeed = 8
    TreasureType = "head"
    baseDurability = 8


# Structural Parts #


class wp_Wrap(wPart):
    traits = {"Material": TEXTILE}
    TreasureType = "simple wrapping"
    baseDurability = 5


class wp_Handle(wPart):
    traits = {"Material": {**METAL, **WOOD}}
    components = {"Grip": wp_Wrap}
    TreasureType = "handle"
    baseDurability = 3


class wp_Pommel(wPart):
    mapDamage = {"Density": 1, "Hardness": 0.8, "Flexibility": 0.5}
    DamageTypes = [0]
    baseDamage = 4
    baseSpeed = 6
    TreasureType = "pommel"
    baseDurability = 3


class wp_Crossguard(wPart):
    TreasureType = "crossguard"
    baseDurability = 6


class wp_Basket(wPart):
    TreasureType = "basket guard"
    baseDurability = 6


class wp_RoundGuard(wPart):
    TreasureType = "round guard"
    baseDurability = 6


# ### WEAPONS ### #


class Weapon_Longsword(Weapon):
    components = {
        "Blade": wp_Slice_2,
        "Handle": wp_Handle,
        "Pommel": wp_Pommel,
        "Guard": wp_Crossguard,
    }
    Weights = ["Blade", "Guard"]  # Weights and counterweights, for
    Counterweights = ["Pommel"]  # determining weapon balance
    TreasureType = "longsword"
    SizeMod = 1.0


class Weapon_Shortsword(Weapon):
    components = {
        "Blade": wp_Slice_2_small,
        "Handle": wp_Handle,
        "Pommel": wp_Pommel,
        "Guard": wp_Crossguard,
    }
    Weights = ["Blade", "Guard"]
    Counterweights = ["Pommel"]
    TreasureType = "shortsword"
    SizeMod = 1.0


class Weapon_Scimitar(Weapon):
    components = {"Blade": wp_Slice_1, "Handle": wp_Handle, "Pommel": wp_Pommel}
    Weights = ["Blade"]  # Weights and counterweights, for
    Counterweights = ["Pommel"]  # determining weapon balance
    TreasureType = "scimitar"
    SizeMod = 1.0


class Weapon_Dagger(Weapon):
    components = {
        "Blade": wp_Slice_1_small,
        "Handle": wp_Handle,
        "Pommel": wp_Pommel,
        "Guard": wp_RoundGuard,
    }
    Weights = ["Blade", "Guard"]
    Counterweights = ["Pommel"]
    TreasureType = "dagger"
    SizeMod = 0.7


class Weapon_Rondel(Weapon):
    components = {
        "Blade": wp_Slice_1_small,
        "Handle": wp_Handle,
        "Pommel": wp_Pommel,
        "Guard": wp_RoundGuard,
    }
    Weights = ["Blade", "Guard"]
    Counterweights = ["Pommel"]
    TreasureType = "rondel"
    SizeMod = 0.7


class Weapon_Greatsword(Weapon):
    components = {
        "Blade": wp_Slice_2,
        "Handle": wp_Handle,
        "Pommel": wp_Pommel,
        "Guard": wp_Crossguard,
    }
    Weights = ["Blade", "Guard"]  # Weights and counterweights, for
    Counterweights = ["Pommel"]  # determining weapon balance
    TreasureType = "greatsword"
    SizeMod = 1.6


def SWORD(*args, **kwargs):
    weps = [
        Weapon_Longsword,
        Weapon_Shortsword,
        Weapon_Scimitar,
        Weapon_Dagger,
        Weapon_Rondel,
        Weapon_Greatsword,
    ]
    return random.choice(weps)(*args, **kwargs)


def asdf(qwert, full=False):
    print(qwert().describe(solo=True, full=full))