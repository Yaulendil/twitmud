from numpy import add as npadd, round

from . import damage, structure
from items.treasure_core import TreasureObject, form_out, choose_from


class Weapon(TreasureObject):
    TreasureType = "Generic Weapon"
    BaseType = "weapon"
    damager = None

    def __init__(self, *args, **kwargs):
        # WEAPONS deal damage determined by their components
        super().__init__(self, *args, **kwargs)
        self.damage = self.calc_damage()

    @property
    def reach(self):
        try:
            r = self.dictComp["Handle"].size
        except:
            r = 0
        try:
            r += self.dictComp[self.damager].size
        except:
            pass
        return r

    def speed(self, base=None):
        base = base or self.dictComp[self.damager].base_speed or 10
        # speed = (1000 * base / self.weight()) / ((self.reach + 1) / 10)
        speed = (1000 * base) / (self.weight() + self.reach)
        # return speed
        return round(speed, 2)

    def calc_size(self):
        s = 1
        return s

    def calc_damage(self):
        d = [0, 0, 0]
        for comp in self.dictComp:
            d = npadd(d, self.dictComp[comp].damage_rating(True))
        return list(d)

    def strself(self, *a, prefix="", **kw):
        """Take the adjectives from the "core" component"""
        try:
            important = self.dictComp[self.damager]
            kw["prefix"] = " ".join([prefix, important.material.__name__])
            kw["adjectives"] = important.get_adj()
        except:
            pass
        return super().strself(*a, **kw)

    def describe(self, solo=True, pad="", full=False):
        o = ""
        if solo:
            o += pad + f"'This is {self}.'"
        d = self.calc_damage()
        dsum = round(sum(d), 2)
        o += form_out(
            "It does "
            # + "/".join([str(round(i, 2)) for i in d])
            + str([str(round(i, 2)) for i in d])
            + " C/P/S damage for "
            + str(dsum)
            + " ideal-total.",
            pad,
        )
        wgh = self.weight()
        spd = self.speed()
        o += form_out(f">> It has a weight of {str(wgh)} "
                      + f"for a speed of {str(spd)}.", pad)
        o += form_out(f">> It does {str(round((dsum + spd) / 10, 2))} DPS.", pad)
        o += super().describe(False, pad, full)
        return o


class Sword(Weapon):
    """A long blade with a handle on one end; Typically swung to slash"""
    components = {
        "Blade": damage.Blade,
        "Pommel": damage.Sphere,
        "Handle": structure.Handle,
        "Guard": [structure.Crossguard, structure.Roundguard],
    }
    TreasureType = "Sword"
    damager = "Blade"


class Greatsword(Sword):
    components = {
        "Blade": damage.BladeBig,
        "Pommel": damage.Sphere,
        "Handle": structure.HandleLong,
        "Guard": structure.Crossguard,
    }
    TreasureType = "Greatsword"


class Dagger(Sword):
    components = {
        "Blade": damage.BladeSmall,
        "Pommel": damage.Sphere,
        "Handle": structure.Handle,
        "Guard": structure.Roundguard,
    }
    TreasureType = "Dagger"


class Glaive(Sword):
    components = {
        "Blade": damage.Blade,
        "Counterweight": damage.Sphere,
        "Handle": structure.HandleLonger,
    }
    TreasureType = "Glaive"


class Club(Weapon):
    """A bludgeon meant to crush bones through hard armor"""

    components = {
        "Head": damage.HeadClub,
        "Handle": structure.HandleLong,
        "Counterweight": [None, damage.Sphere],
    }
    TreasureType = "Club"
    damager = "Head"


class Mace(Club):
    components = {
        "Head": damage.HeadMace,
        "Handle": structure.HandleLong,
        "Counterweight": [None, damage.Sphere],
    }
    TreasureType = "Mace"


class MaceCav(Club):
    components = {
        "Head": damage.HeadMace,
        "Handle": structure.HandleLonger,
        "Counterweight": [None, damage.Sphere],
    }
    TreasureType = "Cavalry Mace"


class Star(Club):
    components = {
        "Head": damage.HeadStar,
        "Handle": structure.HandleLong,
        "Counterweight": [None, damage.Sphere],
    }
    TreasureType = "Star"


class Axe(Weapon):
    components = {
        "Head": damage.HeadAxe,
        "Handle": structure.HandleLong,
        "Counterweight": [None, damage.Sphere],
    }
    TreasureType = "Axe"
    damager = "Head"


class Halberd(Axe):
    components = {
        "Head": damage.HeadAxe,
        "Handle": structure.HandleLonger,
        "Counterweight": [None, damage.Sphere],
    }
    TreasureType = "Halberd"


swords = [Sword, Greatsword, Dagger]
bludgeons = [Club, Mace, Star]
cleavers = [Axe]
polearms = [Glaive, MaceCav, Halberd]

weapons = [swords, bludgeons, cleavers, polearms]


def random_weapon():
    return choose_from(weapons)[0]


def test_weapon(full=False, mat=None):
    for a in weapons:
        for b in a:
            print(b(override_material=mat).describe(full=full))
            print("")
