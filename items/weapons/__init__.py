from numpy import add as npadd, round

from . import damage, structure
from items.treasure_core import TreasureObject, form_out, choose_from


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
            "It does "
            # + "/".join([str(round(i, 2)) for i in d])
            + str([str(round(i, 2)) for i in d])
            + " C/P/S damage for "
            + str(round(sum(d), 2))
            + " ideal-total.",
            pad,
        )
        o += super().describe(False, pad, full)
        return o


class Sword(Weapon):
    """A long blade with a handle on one end; Typically swung to slash"""
    components = {
        "Blade": damage.Blade,
        "Pommel": damage.Sphere,
        "Handle": structure.Handle,
        "Guard": structure.Crossguard,
    }
    TreasureType = "Sword"

    def strself(self, *a, prefix="", **kw):
        """Insert the blade material in front of "Sword" when describing this"""
        important = self.dictComp["Blade"]
        kw["prefix"] = " ".join([prefix, important.material.__name__])
        kw["adjectives"] = important.get_adj()
        return super().strself(*a, **kw)


class Greatsword(Sword):
    components = {
        "Blade": damage.BladeBig,
        "Pommel": damage.Sphere,
        "Handle": structure.HandleLong,
        "Guard": structure.Crossguard,
    }
    TreasureType = "Greatsword"


class Club(Weapon):
    """A bludgeon meant to crush bones through hard armor"""
    components = {
        "Head": damage.HeadClub,
        "Handle": structure.HandleLong,
    }
    TreasureType = "Club"

    def strself(self, *a, prefix="", **kw):
        important = self.dictComp["Head"]
        kw["prefix"] = " ".join([prefix, important.material.__name__])
        kw["adjectives"] = important.get_adj()
        return super().strself(*a, **kw)


class Mace(Club):
    components = {
        "Head": damage.HeadMace,
        "Handle": structure.HandleLong,
    }
    TreasureType = "Mace"


class MaceCav(Club):
    components = {
        "Head": damage.HeadMace,
        "Handle": structure.HandleLonger,
    }
    TreasureType = "Cavalry Mace"


class Star(Club):
    components = {
        "Head": damage.HeadStar,
        "Handle": structure.HandleLong,
    }
    TreasureType = "Star"


def random_weapon():
    return choose_from([Sword, Greatsword, Club, Mace, MaceCav, Star])[0]
