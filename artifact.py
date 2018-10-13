from treasure_core import TreasureObject
from consumables import bottleWater, Potion, Bottle
from materials import METAL, WOOD, GEMSTONE, GLASS


class Weapon(TreasureObject):
    TreasureType = "Generic Weapon"

    def __init__(self, *args, **kwargs):
        self.Damage = 0 # WEAPONS deal damage determined by their components
        super().__init__(self, *args, **kwargs)
        self.calcDamage()

    def calcDamage(self):
        D = 0
        return D

class weaponPart_Slash(TreasureObject):
    mapDamage = {
              "Density":0.5,
              "Hardness":1,
              "Flexibility":2
              }
    traits = {"Material":METAL}
    TreasureType = "blade"

class weaponPart_Thrust(TreasureObject):
    mapDamage = {
              "Density":1,
              "Hardness":2,
              "Flexibility":0.5
              }
    traits = {"Material":METAL}
    TreasureType = "tip"

class weaponPart_Crush(TreasureObject):
    mapDamage = {
              "Density":2,
              "Hardness":1,
              "Flexibility":0.5
              }
    traits = {"Material":METAL}
    TreasureType = "head"

class weaponPart_Handle(TreasureObject):
    traits = {"Material":METAL}
    TreasureType = "handle"

class weaponPart_Pommel(TreasureObject):
    traits = {"Material":METAL}
    TreasureType = "pommel"

class weaponPart_Crossguard(TreasureObject):
    traits = {"Material":METAL}
    TreasureType = "crossguard"

class Weapon_Sword(Weapon):
    components = {"Blade":weaponPart_Slash,
                  "Handle":weaponPart_Handle,
                  "Pommel":weaponPart_Pommel,
                  "Guard":weaponPart_Crossguard}
    TreasureType = "sword"






def asdf(qwert):
    print(qwert().describe())
