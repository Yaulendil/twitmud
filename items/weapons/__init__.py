from numpy import add as npadd, round

from . import damage, structure
from items.treasure_core import TreasureObject, form_out


class Weapon(TreasureObject):
    TreasureType = "Generic Weapon"
    BaseType = "weapon"

    def __init__(self, *args, **kwargs):
        # WEAPONS deal damage determined by their components
        super().__init__(self, *args, **kwargs)
        self.damage = self.calc_damage()

    def calc_size(self):
        s = 1
        return s

    def calc_damage(self):
        d = [0, 0, 0]
        for comp in self.dictComp:
            d = npadd(d, self.dictComp[comp].damage_rating(True))
        return list(d)

    def describe(self, solo=True, pad="", full=False):
        o = ""
        if solo:
            o += pad + f"'This is {self}.'"
        d = self.calc_damage()
        o += form_out(
            f"It does {'/'.join([str(round(i, 2)) for i in d])} C/P/S damage for {round(sum(d), 2)} ideal-total.",
            pad,
        )
        o += super().describe(False, pad, full)
        return o


class Sword(Weapon):
    components = {"Blade": damage.Blade, "Pommel": damage.Sphere, "Handle": structure.Handle, "Guard": structure.Crossguard}
    TreasureType = "Sword"
