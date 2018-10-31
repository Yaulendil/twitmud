"""
Weapon Parts that do not contribute damage. Handles, guards, etc.
"""
from numpy import round, random as npr

from items import materials
from items.treasure_core import TreasureObject
from grammar import form_out


class WPart(TreasureObject):
    size = 10
    traits = {"Material": materials.Metal.decor + materials.Metal.structure}
    TreasureType = "Tool Component"
    base_durability = 5

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        # Base values; Multiplied later
        # self.size = 1
        # # Approximate volume occupied by the component; Affects reach and weight
        self.hp = self.base_durability * self.material.Toughness
        # "Health" of a part determines when it breaks and what its damage adjective is

    def damage_rating(self, split=True):
        # Amount of damage contributed by this component
        d = []
        try:  # FC: Assume the part contributes damage
            # for damage_type, coeffs in self.type_damage.items():
            for damage_type in ["Crush", "Pierce", "Slice"]:
                damage = 0
                # for damage_stat, coeff in self.stat_damage.items():
                # print(self, damage_type + ":")
                stats = self.type_damage.get(damage_type, {})
                for damage_stat, coeff in stats.items():
                    dmore = getattr(self.material, damage_stat) * coeff * self.size
                    # print(str(dmore), "from", getattr(self.material, damage_stat), damage_stat, "(" + self.material.__name__ + ")")
                    damage += dmore
                d.append(damage/100)

            for i in range(len(d)):
                if i in self.DamageTypesGood:
                    d[i] *= self.Effectiveness
                if i in self.DamageTypesBad:
                    d[i] /= self.Effectiveness
                # d[i] = d[i]/100
        except AttributeError:  # FC: It has been found that this part contributes no damage
            d = [0, 0, 0]
        d_out = [round(i, 2) for i in d]
        if not split:
            d_out = sum(d_out)
        return d_out

    def describe(self, solo=True, pad="", full=False):
        o = super().describe(solo, pad, full)
        d = self.damage_rating()
        dstr = [str(n) for n in d]
        if sum(d) > 0:
            o += form_out(f"It contributes {dstr} C/P/S damage.", pad, True)
        return o


class Grip(WPart):
    size = 0.5
    traits = {"Material": materials.Textile.all}
    TreasureType = "simple wrapping"


class GripWide(WPart):
    size = 1.5
    traits = {"Material": materials.Textile.all}
    TreasureType = "long wrapping"


class Handle(WPart):
    size = 3
    traits = {"Material": materials.Metal.structure + materials.Wood.structure}
    components = {"Grip": Grip}
    TreasureType = "straight handle"


class HandleLong(WPart):
    size = 8
    traits = {"Material": materials.Metal.structure + materials.Wood.structure}
    components = {"Grip": GripWide}
    TreasureType = "long handle"


class HandleLonger(WPart):
    size = 14
    traits = {"Material": materials.Metal.structure + materials.Wood.structure}
    components = {"Upper Grip": GripWide,
                  "Lower Grip": Grip}
    TreasureType = "pole"


class Crossguard(WPart):
    size = 4
    TreasureType = "crossguard"


class Roundguard(WPart):
    size = 2
    TreasureType = "round guard"
