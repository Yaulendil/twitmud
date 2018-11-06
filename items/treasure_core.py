import jsonpickle
from numpy import random as npr

from . import materials

jsonpickle.set_encoder_options('simplejson', sort_keys=True, indent=2)
DEBUG = False


def normalize(in_):
    s = sum(in_)
    return [float(i) / s for i in in_]


def choose_from(choices: list, q=1, probability: list = None):
    """
    Choices will be a list. Each item of the list may also be a list or a tuple.
        If an item of Choices is a tuple, it will be a list of subchoices and a list of probabilities.
    Probability will be a list of numbers and overrides a probability list packed with the choices.
    Choose Q objects from Choices and return them.
    """
    if type(choices) not in [tuple, list, range]:
        # If Choices is a single item, return it immediately.
        return choices

    prob = None
    if type(choices) == tuple:
        (choices, prob) = choices

    if not probability:
        probability = prob or [1 for _ in choices]

    if DEBUG:
        print("\nChoices =", [type(x) for x in choices], "\nProbab. =", probability)

    choice: list = npr.choice(
        choices, size=q, replace=False, p=normalize(probability)
    ).tolist()
    for i in range(len(choice)):
        if type(choice[i]) == tuple:
            # If a tuple, 0 is list and 1 is prob; Choose
            choice[i] = choose_from(choice[i][0], 1, choice[i][1])
        while type(choice[i]) == list and len(choice[i]) > 1 and q == 1:
            # If a list of >1, choose one; Repeat
            choice[i] = choose_from(choice[i])
        while type(choice[i]) == list and len(choice[i]) == 1:
            # Remove all recursion from final result
            choice[i] = choice[i][0]
    return choice


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
    additions = {}
    # ADDITIONS: Extra sub-objects added on; Gemstones, precious metal inlay, etc
    materials = []
    # MATERIALS: Possibilities for object materials; May be left blank

    TreasureType = "Generic Treasure"
    BaseType = "item"
    size = 3

    def __init__(self, *args, material=None, **kwargs):
        self.dictAttr = {}
        self.dictTrait = {}
        self.dictComp = {}
        self.dictAdd = {}

        self.adjectives = []
        self.material = (material or choose_from(self.materials)[0]) if self.materials else None

        self.Value = 0
        self.TreasureLabel = None

        self.hp = 100

        dmg = list(range(0,90,9))
        chance = list(range(0,10,1))
        chance.reverse()

        self.dmg = {x: choose_from(dmg, probability=chance)[0] for x in list(materials.Material.dmg_FX)}
        self.aes = {x: choose_from(dmg, probability=chance)[0] for x in list(materials.Material.aes_FX)}

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
        keys = list(self.components.keys())
        comp = self.dictComp.get(keys[key], IndexError(f"{self.__class__.__name__} has no component {key}"))
        if type(comp) == IndexError:
            raise comp
        return comp

    def __setitem__(self, key, value):
        keys = list(self.components.keys())
        self.dictComp[keys[key]] = value

    def __delitem__(self, key):
        keys = list(self.components.keys())
        del self.dictComp[keys[key]]


