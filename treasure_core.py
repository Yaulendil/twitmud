import random
from numpy import random as npr

from grammar import pluralize, get_a, sequence_words

# Traits NOT to list (normally) in *.describe()
NoDescribe = ["Material"]


def form_out(txt, pad="", angle=False):
    ang = {True: "\\", False: "|"}[angle]
    return f"\n{pad}{ang}_'{txt}'"


def set_value(obj, attr, value):
    exec(f"obj.{attr} = value")


def get_value(obj, attr):
    return eval(f"obj.{attr}")


def random_from(src, q=1, d=None, dd=None):
    # q = Desired number of elements from src
    # d = probability distribution
    st = type(src)
    ret = src
    if st == tuple and type(src[1]) == list:
        # If this is a tuple with a list at index 1
        d = src[1]
        src = src[0]
        st = type(src)
    elif dd and not d:
        try:
            d = [dd[k] for k in src]
        except:
            d = None
    if st == dict:
        src = list(src.keys())
        st = type(src)
    if st == list or st == range:  # SRC is one-dimensional? Pick from it.
        ret = npr.choice(src, size=q, replace=False, p=d).tolist()
    return ret


# def rand_attr(obj, attr):
#     try:
#         assert get_value(obj, attr) is None
#     except:
#         strt = obj.attrs[attr][0]  # Minimum number of values
#         stop = obj.attrs[attr][1]  # Maximum number of values
#         poss = obj.attrs[attr][2]  # Possible values (list or dict)
#         q = random.randint(strt, stop)
#         vals = random_from(poss, q)
#         if strt == 1 and stop == 1:
#             obj.dictAttr.update({attr: vals[0]})
#             set_value(obj, attr, vals[0])
#         else:
#             obj.dictAttr.update({attr: vals})
#             set_value(obj, attr, vals)
#
#
# def rand_trait(obj, trait):
#     try:
#         assert get_value(obj, trait) is None
#     except:
#         poss = obj.traits[trait]  # Possible values (list or dict)
#         # val = random.sample(poss,1)[0]
#         val = random_from(poss, None)
#         obj.dictTrait.update({trait: val})
#         set_value(obj, trait, val)
#
#
# def randomize(obj, feat=None, r=False):
#     """Assign all unset attributes, or the given attribute, of an object or component to random possible values.\nIf [r]ecursive, do so for all components as well."""
#     # if not feat in obj.attrs:
#     # return
#     if feat is None:
#         for feat2 in obj.attrs:
#             randomize(obj, feat2)
#         for feat2 in obj.traits:
#             randomize(obj, feat2)
#     else:
#         if feat in obj.attrs:
#             rand_attr(obj, feat)
#         if feat in obj.traits:
#             rand_trait(obj, feat)
#     if r:
#         for sub in obj.dictComp:
#             randomize(obj.dictComp[sub], feat, r)


def shuffle(obj, feat=None, r=False):
    for attr, (amin, amax, poss) in obj.attrs.items():
        if attr == feat or not feat:
            q = random.randint(amin, amax)
            selected = random_from(poss, q)
            obj.dictAttr[attr] = selected
    for trait, poss in obj.traits.items():
        if trait == feat or not feat:
            selected = random_from(poss)[0]
            obj.dictTrait[trait] = selected
    if r:
        for comp, obj2 in obj.dictComp.items():
            shuffle(obj2, feat, r)


class TreasureObject:
    attrs = (
        {}
    )  # ATTRIBUTES: Flavor modifiers, no effect; Any number of a certain attribute type
    # A value in attrs MUST be: a TUPLE or LIST containing: INT1, INT2, LIST1
    # A value in the ATTRDICT of an instance of this class will then be:
    #     - a LIST containing between INT1 and INT2, inclusive, elements from LIST1
    traits = (
        {}
    )  # TRAITS: Defining modifiers, possibly with effects; Exactly one of a given trait
    components = (
        {}
    )  # COMPONENTS: Sub-objects that make up this object; Should be class name
    TreasureType = "Generic Treasure"
    BaseType = "item"

    # Damage FX; Adjectives applied when item is damaged
    dmg_FX = {
        "phys": [
            "dented",
            "chipped",
            "cracked",
            "broken",
        ],
        "burn": ["singed", "charred", "melted"],
    }
    # Aesthetic FX; Adjectives applied when item is cold, bloody, etc
    aes_FX = {
        "cold": [
            "frosted",
            "frozen",
        ],
        "blood": [
            "blood-speckled",
            "blood-spattered",
            "bloody",
            "bloodsoaked",
            "sanguinated",
        ],
    }

    def __init__(self, *args, **kwargs):
        self.dictAttr = {}
        self.dictTrait = {}
        self.dictComp = {}
        self.parent = None

        self.Value = 0
        self.TreasureLabel = None

        self.HP = 100
        self.dmg = {x: 0 for x in list(self.dmg_FX)}
        self.aes = {x: 0 for x in list(self.aes_FX)}

        for comp in self.components:
            c = self.components[comp]()
            self.dictComp.update({comp: c})
            c.parent = self
            # SetValue(self,comp,c)
        shuffle(self)
        # self.__str__ = self.strself
        # self.Appraise()

    def get_adj(self):
        return []

    def strself(self, *, use_generic=False, adjectives=None):
        if adjectives is None:
            adjectives = []
        generic = get_a(str(self.TreasureType), True)
        if use_generic:
            n = generic
        n = self.TreasureLabel or generic
        adj = sequence_words(self.get_adj() + adjectives)
        return " ".join([adj, n])

    def __str__(self):
        return self.strself()

    def describe(self, solo=True, pad="", full=False):
        o = ""
        if solo:
            o += pad + f"'This is {self}.'"
        for a in self.dictAttr:  # Print object attributes (variable number)
            aa = sequence_words(self.dictAttr[a])
            if aa != "":
                o += form_out(f"Its {a.lower()} is {aa}.", pad)
        for a in self.dictTrait:  # Print object traits (one of each)
            if a not in NoDescribe:
                o += form_out(f"Its {a.lower()} is {self.dictTrait[a]}.", pad)
        for a in self.dictComp:  # Describe sub-objects
            aa = self.dictComp[a]
            adesc = aa.describe(solo=False, pad=pad + "|", full=full)
            try:
                mat = aa.dictTrait["Material"]
                try:
                    mat = mat.Adjective
                except:
                    pass
                # if len(aa.dictTrait) <= 1:
                if adesc.count("\n") < 1 and not full:
                    continue
                o += form_out(
                    f"Its {a.lower()} is {self.dictComp[a]} of {mat}.", pad, True
                )
            except:
                o += form_out(f"Its {a.lower()} is {self.dictComp[a]}.", pad, True)
            o += adesc

        return o

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
