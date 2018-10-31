import random
from numpy import random as npr

import grammar

# Traits NOT to list (normally) in *.describe()
NoDescribe = ["Material"]


def form_out(txt, pad="", angle=False):
    ang = {True: "\\", False: "|"}[angle]
    return f"\n{pad}{ang}_'{txt}'"


def set_value(obj, attr, value):
    exec(f"obj.{attr} = value")


def get_value(obj, attr):
    return eval(f"obj.{attr}")


def normalize(in_):
    s = sum(in_)
    return [float(i) / s for i in in_]


def choose_from(choices: list, q=1, probability: list = None):
    """
    Choices will be a list. Each item of the list may also be a list or a tuple.
        If an item of Choices is a tuple, it will be a list of subchoices and a list of probabilities.
    Probability will be a list of numbers.
    Choose Q objects from Choices and return them.
    """
    if not probability:
        probability = [1 for _ in choices]

    choice: list = npr.choice(choices, size=q, replace=False, p=normalize(probability)).tolist()
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
            q = npr.randint(amin, amax+1)
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
    additions = (
        {}
    )  # ADDITIONS: Extra sub-objects added on; Gemstones, precious metal inlay, etc
    TreasureType = "Generic Treasure"
    BaseType = "item"

    # Damage FX; Adjectives applied when item is damaged
    dmg_FX = {
        "phys": ["dented", "chipped", "cracked", "broken"],
        "burn": ["singed", "charred", "melted"],
    }
    # Aesthetic FX; Adjectives applied when item is cold, bloody, etc
    aes_FX = {
        "cold": ["frosted", "frozen"],
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
        generic = grammar.get_a(str(self.TreasureType), True)
        if self.TreasureLabel and not use_generic:
            n = self.TreasureLabel
        else:
            n = generic
        adj = grammar.sequence_words(self.get_adj() + adjectives)
        return " ".join([adj, n]).strip()

    def __str__(self):
        return self.strself()

    def describe(self, solo=True, pad="", full=False):
        o = ""
        if solo:
            o += pad + f"'This is {self}.'"
        for a in self.dictAttr:  # Print object attributes (variable number)
            aa = grammar.sequence_words(self.dictAttr[a])
            if aa != "":
                o += form_out(f"Its {a.lower()} is {str(aa)}.", pad)
        for a in self.dictTrait:  # Print object traits (one of each)
            if a not in NoDescribe:
                o += form_out(
                    f"Its {a.lower()} is {grammar.sequence_words(self.dictTrait[a])}.", pad
                )
        for a, aa in self.dictComp.items():  # Describe sub-objects
            # aa = self.dictComp[a]
            adesc = aa.describe(solo=False, pad=pad + " ", full=full)
            try:
                mat = aa.dictTrait["Material"]
                try:
                    mat = mat.Adjective
                except:
                    mat = mat.__name__
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
