import random

from materials import METAL, WOOD, GEMSTONE, GLASS


def SetValue(obj, attr, value):
    exec(f"obj.{attr} = value")

def GetValue(obj, attr):
    return eval(f"obj.{attr}")


def SequenceWords(words, o=""):
    o1 = ""
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

def randomize(obj, attr=None, r=False):
    """Assign all unset attributes, or the given attribute, of an object or component to random possible values.\nIf [r]ecursive, do so for all components as well."""
    #if not attr in obj.attrs:
        #return
    if attr == None:
        for attr2 in obj.attrs:
            randomize(obj, attr2)
    else:
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
    if r:
        for sub in obj.components:
            randomize(sub, attr, r)


class TreasureObject:
    attrs = {} # ATTRIBUTES: Flavor modifiers, no effect; Any number of a certain attribute type
    traits = {} # TRAITS: Defining modifiers, possibly with effects; Exactly one of a given trait
    components = {} # COMPONENTS: Sub-objects that make up this object; Should be class name

    def __init__(self, *args, **kwargs):
        self.attrDict = {}
        self.compDict = {}
        self.parent = None

        self.Value = 0

        for comp in self.components:
            c = self.components[comp]()
            self.compDict.update({comp:c})
            c.parent = self
            SetValue(self,comp,c)
        #for attr in self.attrs:
            #SetValue(self,attr,None)
        randomize(self)
        self.Appraise()

    def describe(self, solo=True):
        



class potionFluid(TreasureObject):
    attrs = {"Color":(1,1,["red","ruby","orange",
                           "yellow","golden","green","emerald",
                           "blue","cyan","sky","turquoise",
                           "indigo","sapphire","midnight",
                           "purple","violet","amethyst",
                           "black","tar","pitch","coal",
                           "white","milky","silvery"]),
             "Visual":(1,1,["opaque","cloudy","clear","murky"]),
             "Texture":(1,1,["thick","thin","lumpy",
                             "smooth","chunky","pulpy"]),
             "Effect":(0,2,["smoking","steaming",
                            "sparkling","bubbling",
                            "glowing","humming"])}

    def describe(self, solo=True):
        o = "{v}{c} fluid"
        if not solo:
            return o.format(v = " "+self.attrDict["Visual"], c = " "+self.attrDict["Color"])
        l1 = [self.attrDict["Texture"]] + self.attrDict["Effect"]
        s = SequenceWords(l1)
        if s != "":
            o = o + " is " + s
        o = "The"+o+"."
        return o.format(v = " "+self.attrDict["Visual"], c = " "+self.attrDict["Color"])

class potionBottle(TreasureObject):
    components = {"Contents":potionFluid}
    attrs = {"Material":(1,1,["glass","crystal","plastic"]),
             "Fullness":(1,1,range(20,100,5)),
             "Vessel":(1,1,["bottle","flask","vial"]),
             "Shape":(1,1,["spherical","tetrahedric","cubic","octohedric","decahedric","dodecahedric","icosahedric"])}

    def describe(self, solo=True):
        o = "This {Shape} {Material} {Vessel} is {Fullness}% full.".format(**self.attrDict)
        for sub in self.compDict:
            o = o + "\n    " + self.compDict[sub].describe().replace("fluid","fluid within")
        return o

class Potion(TreasureObject):
    components = {"Bottle":potionBottle}






class Weapon(TreasureObject):
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

class weaponPart_Thrust(TreasureObject):
    mapDamage = {
              "Density":1,
              "Hardness":2,
              "Flexibility":0.5
              }
    Materials = METAL.copy()

class weaponPart_Crush(TreasureObject):
    mapDamage = {
              "Density":2,
              "Hardness":1,
              "Flexibility":0.5
              }
    Materials = METAL.copy()

#class weaponPart_Handle(TreasureObject):
    #components = 
