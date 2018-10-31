from numpy import add as npadd

from . import damage, structure
from treasure_core import TreasureObject, form_out


class Weapon(TreasureObject):
    TreasureType = "Generic Weapon"
    BaseType = "weapon"

    def __init__(self, *args, **kwargs):
        self.damage = [0, 0, 0]  # WEAPONS deal damage determined by their components
        super().__init__(self, *args, **kwargs)
        self.calc_damage()

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
            f"It does {'/'.join([str(i) for i in d])} C/P/S damage for {sum(d)} ideal-total.",
            pad,
        )
        o += super().describe(False, pad, full)
        return o


class Sword(Weapon):
    # components = {"Blade": damage.Blade, "Handle": None, "Pommel": None, "Guard": None}
    components = {"Blade": damage.Blade}
    TreasureType = "Sword"
