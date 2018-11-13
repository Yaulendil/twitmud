from numpy import add as npadd

from . import damage, structure
from items.treasure_core import TreasureObject
from items import util
from selection import choose_from


class Weapon(TreasureObject):
    TreasureType = "Generic Weapon"
    BaseType = "weapon"

    def __init__(self, *args, **kwargs):
        # WEAPONS deal damage determined by their components
        super().__init__(self, *args, **kwargs)
        self.damage = 0
        self.calc_damage()

    @property
    def reach(self):
        try:
            r = self.dictComp["Handle"].size
        except:
            r = 0
        try:
            r += self.dictComp[self.primary].size
        except:
            pass
        return r

    def speed(self, base=None):
        base = base or self.dictComp[self.primary].base_speed or 10
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
        self.damage = [round(float(dd), 2) for dd in list(d)]
        return self.damage


class Sword(Weapon):
    """A long blade with a handle on one end; Typically swung to slash"""

    components = {
        "Blade": damage.Blade,
        "Guard": [structure.Crossguard, structure.Roundguard],
        "Handle": structure.Handle,
        "Pommel": damage.Sphere,
    }
    TreasureType = "Sword"
    primary = "Blade"


class Greatsword(Sword):
    components = {
        "Blade": damage.BladeBig,
        "Guard": structure.Crossguard,
        "Handle": structure.HandleLong,
        "Pommel": damage.Sphere,
    }
    TreasureType = "Greatsword"


class Falchion(Sword):
    components = {
        "Blade": damage.BladeCurved,
        "Guard": structure.Roundguard,
        "Handle": structure.Handle,
        "Pommel": damage.Sphere,
    }
    TreasureType = "Falchion"


class GreatswordCurved(Sword):
    components = {
        "Blade": damage.BladeCurvedBig,
        "Guard": structure.Crossguard,
        "Handle": structure.HandleLong,
        "Pommel": damage.Sphere,
    }
    TreasureType = "Curved Greatsword"


class Glaive(Sword):
    components = {
        "Blade": damage.BladeCurved,
        "Handle": structure.HandleLonger,
        "Counterweight": damage.Sphere,
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
    primary = "Head"


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
    primary = "Head"


class Halberd(Axe):
    components = {
        "Head": damage.HeadHalberd,
        "Handle": structure.HandleLonger,
        "Counterweight": [None, damage.Sphere],
    }
    TreasureType = "Halberd"


class Pike(Weapon):
    components = {
        "Point": damage.Spike,
        "Handle": structure.HandleLonger,
        "Counterweight": [None, damage.Sphere],
    }
    TreasureType = "Pike"
    primary = "Point"


swords = [Sword, Falchion, Greatsword, GreatswordCurved]
bludgeons = [Club, Mace, Star]
cleavers = [Axe]
polearms = [Glaive, MaceCav, Halberd, Pike]

weapons = [swords, bludgeons, cleavers, polearms]


def random_weapon():
    return choose_from((weapons, [len(x) for x in weapons]))[0]


def test_weapon(minimal=False, mat=None, norecurse=False, images=True, text=True):
    sets = []
    for a in weapons:
        imgs = []
        for b in a:
            bb = b(override_material=mat)
            if text:
                util.describe_item(bb, minimal=minimal, norecurse=norecurse, images=images)
            else:
                imgs.append(util.item_image(bb))
        sets.append(imgs)

    if sets and not text:
        list_of_lists = [util.combine_images(imgs) for imgs in sets]
        list_of_strings = util.combine_images(list_of_lists, " │ ")
        print("\n".join(list_of_strings))
