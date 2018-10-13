import random

from materials import METAL, WOOD, GEMSTONE, GLASS


def SetValue(obj, attr, value):
    exec(f"obj.{attr} = value")

def GetValue(obj, attr):
    return eval(f"obj.{attr}")

def SequenceWords(words, o=""):
    o1 = ""
    #print(f"Sequencing '{words}'")
    if len(words) == 0:
        pass
    elif len(words) == 1:
        o = o+"{}".format(words.pop(0))
    elif len(words) > 1:
        o = o+"{}".format(words.pop(0))
        if len(words) > 1:
            o1 = ", and {}".format(words.pop(-1))
        else:
            o1 = " and {}".format(words.pop(-1))
        for p in words:
            o = o+", {}".format(p)
    return o + o1

# Given grammar and a number, return the appropriate singular or plural form
def Pluralize(n,p="s",s="",w=""):
    return w+{True:p,False:s}[n!=1]

def GetA(word):
    first = word.lower()[0]
    if first in "aeiou":
        return "an"
    else:
        return "a"

def randAttr(obj, attr):
    try:
        assert GetValue(obj,attr) == None
    except:
        strt = obj.attrs[attr][0] # Minimum number of values
        stop = obj.attrs[attr][1] # Maximum number of values
        poss = obj.attrs[attr][2] # Possible values (list or dict)
        vals = random.sample(poss,random.randrange(strt,stop+1))
        if strt == 1 and stop == 1:
            obj.attrDict.update({attr:vals[0]})
            SetValue(obj, attr, vals[0])
        else:
            obj.attrDict.update({attr:vals})
            SetValue(obj, attr, vals)

def randTrait(obj, trait):
    try:
        assert GetValue(obj,trait) == None
    except:
        poss = obj.traits[trait] # Possible values (list or dict)
        val = random.sample(poss,1)[0]
        obj.traitDict.update({trait:val})
        SetValue(obj, trait, val)

def randomize(obj, feat=None, r=False):
    """Assign all unset attributes, or the given attribute, of an object or component to random possible values.\nIf [r]ecursive, do so for all components as well."""
    #if not feat in obj.attrs:
        #return
    if feat == None:
        for feat2 in obj.attrs:
            randomize(obj, feat2)
        for feat2 in obj.traits:
            randomize(obj, feat2)
    else:
        if feat in obj.attrs:
            randAttr(obj,feat)
        if feat in obj.traits:
            randTrait(obj,feat)
    if r:
        for sub in obj.compDict:
            randomize(obj.compDict[sub], feat, r)


class TreasureObject:
    attrs = {} # ATTRIBUTES: Flavor modifiers, no effect; Any number of a certain attribute type
    traits = {} # TRAITS: Defining modifiers, possibly with effects; Exactly one of a given trait
    components = {} # COMPONENTS: Sub-objects that make up this object; Should be class name
    TreasureType = "Generic Treasure"

    def __init__(self, *args, **kwargs):
        self.attrDict = {}
        self.traitDict = {}
        self.compDict = {}
        self.parent = None

        self.Value = 0
        self.TreasureLabel = None

        for comp in self.components:
            c = self.components[comp]()
            self.compDict.update({comp:c})
            c.parent = self
            SetValue(self,comp,c)
        #for attr in self.attrs:
            #SetValue(self,attr,None)
        randomize(self)
        #self.Appraise()

    def __str__(self, *, UseGeneric=False):
        generic = GetA(str(self.TreasureType)) + " " + self.TreasureType
        if UseGeneric:
            return generic
        return self.TreasureLabel or generic

    #def desc(self, solo=True, pad=""):
        #o = ""
        #if solo:
            #o = o + f"This is a {self}."
        #p1 = pad + " "
        #for q in self.attrDict:
            #o = o + f" Its {q} is {self.attrDict[q]}."
        #for q in self.traitDict:
            #o = o + f"\nIts {q} is {self.traitDict[q]}."
        #return o

    #def describe(self, solo=True, pad=""):
        #o = self.desc(solo,pad)
        #p4 = pad + "    "
        #for q in self.compDict:
            #o += "\n" + self.compDict[q].describe(False,p4)
        #return o

    def describe(self, solo=True, pad=""):
        o = ""
        if solo:
            o += pad + f"This is {self}."
        for a in self.attrDict:
            aa = SequenceWords(self.attrDict[a])
            if aa != "":
                o += f"\n{pad}- Its {a} is {aa}."
        for a in self.traitDict:
            o += f"\n{pad}- Its {a} is {self.traitDict[a]}."
        for a in self.compDict:
            o += f"\n{pad}- Its {a} is {self.compDict[a]}."
            o += self.compDict[a].describe(solo=False, pad = pad + "  ")


        return o



class potionFluid(TreasureObject):
    attrs = {"Effect":(0,2,["smoking","steaming",
                            "sparkling","bubbling",
                            "glowing","humming"])}
    traits = {"Color":["red","ruby","orange",
                       "yellow","golden","green","emerald",
                       "blue","cyan","sky","turquoise",
                       "indigo","sapphire","midnight",
                       "purple","violet","amethyst",
                       "black","tar","pitch","coal",
                       "white","milky","silvery",
                       "chocolate","woody","mocha"],
             "Visual":["opaque","cloudy","clear","murky"],
             "Texture":["thick","thin","lumpy",
                        "smooth","chunky","pulpy"]}
    TreasureType = "strange fluid"

    #def desc(self, solo=True, pad=""):
        #o = "{v}{c} fluid"
        ##if not solo:
            ##return o.format(v = " "+self.attrDict["Visual"], c = " "+self.attrDict["Color"])
        #l1 = [self.attrDict["Texture"]] + self.attrDict["Effect"]
        #s = SequenceWords(l1)
        #if s != "":
            #o += " is " + s
        #o = "The"+o+"."
        #return o.format(v = " "+self.attrDict["Visual"], c = " "+self.attrDict["Color"])

class potionBottle(TreasureObject):
    components = {"Contents":potionFluid}
    traits = {"Material":["glass","crystal","plastic"],
             "Fullness":range(20,100,5),
             #"Vessel":["bottle","flask","vial"],
             "Shape":["spherical","tetrahedric","cubic","octohedric","decahedric","dodecahedric","icosahedric"]}
    TreasureType = "potion bottle"

    #def desc(self, solo=True, pad=""):
        #o = "The {Shape} {Material} {Vessel} is {Fullness}% full.".format(**self.attrDict)
        #for sub in self.compDict:
            #o += "\n    " + self.compDict[sub].describe().replace("fluid","fluid within")
        #return o

    #def describe(self, solo=True, pad=""):
        #o = self.desc(solo,pad)
        #return o

class Potion(TreasureObject):
    components = {"Bottle":potionBottle}
    TreasureType = "potion"


class fluidWater(potionFluid):
    attrs = {}
    traits = {"Color":["blue"],
             "Visual":["cloudy","clear","murky"]}
             #"Texture":["thick","thin","lumpy",
                        #"smooth","chunky","pulpy"]}
    TreasureType = "water"

class bottleWater(potionBottle):
    components = {"Contents":fluidWater}
    TreasureType = "water bottle"




class Weapon(TreasureObject):
    TreasureType = "Generic Weapon"

    def __init__(self, *args, **kwargs):
        self.Damage = 0 # WEAPONS deal damage determined by their components
        super().__init__(self, *args, **kwargs)
        self.calcDamage()

    def calcDamage(self):
        D = 0
        return D

class weaponPart_Slash(TreasureObject):
    mapDamage = {
              "Density":0.5,
              "Hardness":1,
              "Flexibility":2
              }
    Materials = METAL.copy()
    TreasureType = "blade"

class weaponPart_Thrust(TreasureObject):
    mapDamage = {
              "Density":1,
              "Hardness":2,
              "Flexibility":0.5
              }
    Materials = METAL.copy()
    TreasureType = "tip"

class weaponPart_Crush(TreasureObject):
    mapDamage = {
              "Density":2,
              "Hardness":1,
              "Flexibility":0.5
              }
    Materials = METAL.copy()
    TreasureType = "head"

class weaponPart_Handle(TreasureObject):
    #components = 
    pass

class Weapon_Sword(Weapon):
    components = {"Blade":weaponPart_Slash,
                  "Handle":weaponPart_Handle}
    TreasureType = "Sword"
