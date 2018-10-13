import random
from numpy import add as npadd

from treasure_core import TreasureObject, FormOut
from consumables import bottleWater, Potion, Bottle
from materials import METAL, WOOD, GEMSTONE, GLASS, TEXTILE


class Weapon(TreasureObject):
    TreasureType = "Generic Weapon"

    def __init__(self, *args, **kwargs):
        self.Damage = 0 # WEAPONS deal damage determined by their components
        super().__init__(self, *args, **kwargs)
        self.calcDamage()

    def calcSize(self):
        S = 1
        return S

    def calcDamage(self):
        D = [0,0,0]
        for comp in self.dictComp:
            D = npadd(D,self.dictComp[comp].damageRating(True))
        return list(D)

    def describe(self, solo=True, pad=""):
        o = ""
        if solo:
            o += pad + f"'This is {self}.'"
        D = self.calcDamage()
        o += FormOut(f"It does {'/'.join([str(i) for i in D])} C/P/S damage for {sum(D)} ideal-total.",pad)
        o += super().describe(False,pad)
        return o

def DB(*args):
    print(*args,sep=" // ")

class wPart(TreasureObject):
    TreasureType = "Weapon Component"
    baseDurability = 5

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        # Base values; Multiplied later
        self.Size = 1 # Approximate volume occupied by the component; Affects reach and weight
        self.HP = self.baseDurability * self.MatStat["Toughness"] # "Health" of a part determines when it breaks and what its damage modifier says

    @property
    def MatStat(self):
        test = self.traits["Material"]
        if type(test) == tuple:
            test = test[0]
        test = test[self.dictTrait["Material"]] # Get the base stat table
        return test
        """
        {"Value":10, # Monetary worth of the material
         "Density":10, # How much mass is in a given volume; Weapon weight
         "Hardness":10, # How well a weapon maintains shape; Aids sharpness
         "Toughness":10, # Difficulty to permanently deform; Durability
         "Flexibility":10}, # Ability to temporarily deform
        """

    def damageRating(self,split=False): # Amount of damage contributed by this component
        D = 0
        try:
            dBase = self.MatStat # Damage bases
            dScale = self.mapDamage # Damage scale factors
            #DB(self,dBase,dScale)
            if split:
                D = []
            for n in dScale: # Do the following for EACH STAT and then sum them
                #DB(n,dScale[n],D)
                if split:
                    D.append(float(dScale[n] # wp.mapDamage["Density"] (0.5)
                        * dBase[n])) #  MULTIPLIED by dBase["Density"] (10)
                else:
                    D += (dScale[n] #        wp.mapDamage["Density"] (0.5)
                        * dBase[n]) # MULTIPLIED by dBase["Density"] (10)
        except Exception as e:
            D = 0
            #DB(e)
        return D

    def describe(self, solo=True, pad=""):
        o = super().describe(solo,pad)
        D = self.damageRating(True)
        if D != 0:
            o += FormOut(f"It contributes {D} C/P/S damage.",pad,True)
        return o

# Damage-dealing Parts #

# Slashing weapons; Longswords, daggers, etc
class wp_Slash_1(wPart):
    mapDamage = {
              "Density":0.5,
              "Hardness":1,
              "Flexibility":2
              }
    baseDamage = 10
    baseSpeed = 14
    traits = {"Material":METAL}
    TreasureType = "single-edged blade"
    baseDurability = 5

class wp_Slash_1_small(wp_Slash_1):
    baseDamage = 6
    baseSpeed = 20
    TreasureType = "short single-edged blade"

class wp_Slash_2(wPart):
    mapDamage = {
              "Density":0.5,
              "Hardness":1,
              "Flexibility":2
              }
    baseDamage = 12
    baseSpeed = 12
    traits = {"Material":METAL}
    TreasureType = "double-edged blade"
    baseDurability = 5

class wp_Slash_2_small(wp_Slash_2):
    baseDamage = 6
    baseSpeed = 20
    TreasureType = "short double-edged blade"

# Thrusting weapons; Rapiers, spears, etc
class wp_Thrust(wPart):
    mapDamage = {
              "Density":1,
              "Hardness":2,
              "Flexibility":0.5
              }
    baseDamage = 12
    baseSpeed = 16
    traits = {"Material":METAL}
    TreasureType = "tip"
    baseDurability = 6

# Thrusting weapons; Rapiers, spears, etc
class wp_ThrustBlade(wPart):
    mapDamage = {
              "Density":1,
              "Hardness":2,
              "Flexibility":0.5
              }
    baseDamage = 12
    baseSpeed = 16
    traits = {"Material":METAL}
    TreasureType = "edgeless blade"
    baseDurability = 6

# Blunt weapons; Maces, hammers, etc
class wp_Crush(wPart):
    mapDamage = {
              "Density":2,
              "Hardness":1,
              "Flexibility":0.5
              }
    baseDamage = 12
    baseSpeed = 8
    traits = {"Material":METAL}
    TreasureType = "head"
    baseDurability = 8

# Structural Parts #

class wp_Wrap(wPart):
    traits = {"Material":TEXTILE}
    TreasureType = "simple wrapping"
    baseDurability = 5

class wp_Handle(wPart):
    traits = {"Material":METAL}
    components = {"Grip":wp_Wrap}
    TreasureType = "handle"
    baseDurability = 3



class wp_Pommel(wPart):
    traits = {"Material":METAL}
    TreasureType = "pommel"
    baseDurability = 3



class wp_Crossguard(wPart):
    traits = {"Material":METAL}
    TreasureType = "crossguard"
    baseDurability = 6

class wp_Basket(wPart):
    traits = {"Material":METAL}
    TreasureType = "basket guard"
    baseDurability = 6

class wp_RoundGuard(wPart):
    traits = {"Material":METAL}
    TreasureType = "round guard"
    baseDurability = 6


# ### WEAPONS ### #


class Weapon_Longsword(Weapon):
    components = {"Blade":wp_Slash_2,
                  "Handle":wp_Handle,
                  "Pommel":wp_Pommel,
                  "Guard":wp_Crossguard}
    Weights = ["Blade","Guard"] # Weights and counterweights, for
    Counterweights = ["Pommel"] #     determining weapon balance
    TreasureType = "longsword"
    SizeMod = 1.0

class Weapon_Shortsword(Weapon):
    components = {"Blade":wp_Slash_2_small,
                  "Handle":wp_Handle,
                  "Pommel":wp_Pommel,
                  "Guard":wp_Crossguard}
    Weights = ["Blade","Guard"]
    Counterweights = ["Pommel"]
    TreasureType = "shortsword"
    SizeMod = 1.0

class Weapon_Dagger(Weapon):
    components = {"Blade":wp_Slash_1_small,
                  "Handle":wp_Handle,
                  "Pommel":wp_Pommel,
                  "Guard":wp_RoundGuard}
    Weights = ["Blade","Guard"]
    Counterweights = ["Pommel"]
    TreasureType = "dagger"
    SizeMod = 0.7

class Weapon_Rondel(Weapon):
    components = {"Blade":wp_Slash_1_small,
                  "Handle":wp_Handle,
                  "Pommel":wp_Pommel,
                  "Guard":wp_RoundGuard}
    Weights = ["Blade","Guard"]
    Counterweights = ["Pommel"]
    TreasureType = "dagger"
    SizeMod = 0.7



def SWORD(*args,**kwargs):
    weps = [Weapon_Longsword,Weapon_Shortsword,Weapon_Dagger]
    return random.choice(weps)(*args,**kwargs)


def asdf(qwert):
    print(qwert().describe())
