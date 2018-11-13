import jsonpickle
from numpy import random as npr, square

from . import materials
from selection import choose_from

DEBUG = False


def shuffle(obj, feat=None, r=False):
    for attr, (amin, amax, poss) in obj.attrs.items():
        if attr == feat or not feat:
            q = npr.randint(amin, amax + 1)
            selected = choose_from(poss, q)
            obj.dictAttr[attr] = selected
    for trait, poss in obj.traits.items():
        if trait == feat or not feat:
            selected = choose_from(poss)[0]
            obj.dictTrait[trait] = selected
    for dec in obj.additions:
        selected = choose_from(dec)[0]
        if selected and (
            obj.material in selected.material_restrict or not selected.material_restrict
        ):
            obj.decor.append(selected(obj.material))
    if r:
        for comp, obj2 in obj.dictComp.items():
            shuffle(obj2, feat, r)


class TreasureObject:
    attrs = {}
    # ATTRIBUTES: Flavor modifiers, no effect; Any number of a certain attribute type
    # A value in attrs MUST be: a TUPLE or LIST containing: INT1, INT2, LIST1
    # A value in the ATTRDICT of an instance of this class will then be:
    #     - a LIST containing between INT1 and INT2, inclusive, elements from LIST1
    traits = {}
    # TRAITS: Defining modifiers, possibly with effects; Exactly one of a given traitz
    components = {}
    # COMPONENTS: Sub-objects that make up this object; Should be class name
    additions = []
    # ADDITIONS: Extra sub-objects added on; Gemstones, precious metal inlay, etc
    materials = []
    # MATERIALS: Possibilities for object materials; May be left blank

    TreasureType = "Generic Treasure"
    BaseType = "item"
    class_flags = []
    size = 3

    # If this item is a composite item, primary should be the name of the "main" part;
    # For example, the blade of a sword, or the bottle of a beverage
    primary = None

    def __init__(self, *args, material=None, **kwargs):
        self.dictAttr = {}
        self.dictTrait = {}
        self.dictComp = {}
        self.adjectives = []
        self.decor = []

        # Going to experiment with Dwarf Fortress style tokens here
        self.flags = set(self.class_flags)

        try:
            self._material = (
                (material or choose_from(self.materials)[0]) if self.materials else None
            )
        except:
            pass

        self.Value = 0
        self.TreasureLabel = None

        self.hp = 100

        dmg = list(range(0, 90, 10))
        chance = list(square(range(1, 10)))
        chance.reverse()  # Lower values more likely

        self.dmg = {
            x: choose_from(dmg, probability=chance)[0]
            for x in list(materials.Material.dmg_FX)
        }
        self.aes = {
            x: 0
            # x: choose_from(dmg, probability=chance)[0]
            for x in list(materials.Material.aes_FX)
        }

        for comp, v in self.components.items():
            if type(v) == list:
                choice = choose_from(v)[0]
                if not choice:
                    continue
            else:
                choice = v
            c = choice(*args, **kwargs)
            self.dictComp[comp] = c
        shuffle(self)

    @property
    def material(self):
        mat = getattr(self.dictComp.get(self.primary, None), "_material", None)
        return mat or getattr(self, "_material", None)

    def get_adj(self, other=None):
        adjs = []
        targ = other or self

        if targ.material:
            for k, v in targ.material.dmg_FX.items():
                desc = [""] + v
                thresholds = [int((100 / len(desc)) * i) for i in range(len(desc))]
                adj = ""
                for i in range(len(desc)):
                    if targ.dmg[k] > thresholds[i]:
                        adj = desc[i]
                adjs.append(adj)

            for k, v in targ.material.aes_FX.items():
                desc = [""] + v
                thresholds = [int((100 / len(desc)) * i) for i in range(len(desc))]
                adj = ""
                for i in range(len(desc)):
                    if targ.aes[k] > thresholds[i]:
                        adj = desc[i]
                adjs.append(adj)

        while "" in adjs:
            adjs.remove("")

        return adjs

    def weight(self):
        w = 0
        try:
            w += self.size * self.material.Density
        except:
            pass
        for k, v in self.dictComp.items():
            w += v.weight()
        return w

    def serialize(self):
        return jsonpickle.encode(self)

    def save(self, fname):
        jsonpickle.set_encoder_options("simplejson", indent=4 if DEBUG else 0)
        with open(fname, "w") as fh:
            fh.write(self.serialize())

    def clone(self, fulldata=True):
        """
        Create a clone of this object, but not necessarily with any non-obvious
            information maintained
        NOTE: If a user knowledge system is ever implemented, this could
            be used to create a "knowledge model", an INCOMPLETE representation
            of the object which may still hold secrets; for example, the kill
            history or given name of a historical sword
        """
        pass

    def __getitem__(self, key):
        keys = list(self.components)
        comp = self.dictComp.get(keys[key], None)
        if type(comp) == IndexError:
            raise IndexError(f"{self.__class__.__name__} has no component {key}")
        return comp

    def __setitem__(self, key, value):
        keys = list(self.components)
        self.dictComp[keys[key]] = value

    def __delitem__(self, key):
        keys = list(self.components)
        comp = self.dictComp.get(keys[key], None)
        if comp:
            del self.dictComp[keys[key]]
