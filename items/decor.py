"""
DECOR is a stylistic modifier that adds MULTIPLIED VALUE of a material.
An example: Woven leather strips, due to the necessary labor increase, make a tool handle far more luxurious than a crude leather wrapping.
Decor has no impact on stats.
"""
from selection import choose_from
from items import materials
# from .treasure_core import TreasureObject


class Decor:
    value_add = 1
    __adj__ = "Decorated"
    removable = False  # Can it be removed by hand, without tools?

    # These are the only materials this can BE (Blank is NONE)
    materials = []

    # These are the only materials this can GO ON (Blank is ANY)
    material_restrict = []

    def __init__(self, applied=None, material=None):
        self.applied_to = applied
        if material:
            self.material = material
        elif self.materials:
            self.material = choose_from(self.materials)[0]
        else:
            self.material = None

    def as_pverb(self):
        o = f"is {self.__adj__.lower()}"
        if self.material:
            o += f" with {self.material.__name__.lower()}"
        return o


#####################
# Metal Decorations #
#####################
# These involve metal


class MetalInlay(Decor):
    """A design is etched into the object and metal is put in the etching"""

    value_add = 3
    __adj__ = "Inlaid"
    materials = materials.Metal.decor


class MetalPlating(Decor):
    """The surface of this object is a thin layer of decorative metal"""

    value_add = 2.5
    __adj__ = "Plated"
    materials = materials.Metal.decor


class MetalFoil(Decor):
    """Foil wrapping, like a Champagne bottle"""

    value_add = 2.5
    __adj__ = "foil-wrapped"
    removable = True
    materials = materials.Metal.decor

    def as_pverb(self):
        o = f"is {self.__adj__.lower()}"
        if self.material:
            o += f" with {self.material.__name__.lower()} foil"
        return o


class GemEncrust(Decor):
    """Small gemstones are embedded into the surface of this object"""

    value_add = 5
    __adj__ = "Encrusted"
    materials = materials.Gemstone.all


#########################
# Intrinsic Decorations #
#########################
# These have been done to the object to permanently alter it


class Carved(Decor):
    """This wooden object is carved with very intricate designs"""

    value_add = 1.5
    __adj__ = "Intricately Carved"
    material_restrict = materials.Wood.all


class Woven(Decor):
    """This textile surface is composed of straps or bands, neatly woven together"""

    value_add = 1.5
    __adj__ = "Finely Woven"
    material_restrict = materials.Textile.all


########################
# Additive Decorations #
########################
# These are things that have been added to the object


class Basket(Decor):
    """This glass bottle has a straw wrapping around the base"""

    __adj__ = "Basketed"
    removable = True
    material_restrict = materials.Fragile.clear

    def as_pverb(self):
        return "has a straw basket around it"


class Color(Decor):
    """Paint, dye, stain..."""

    __adj__ = "Painted"
    material_restrict = materials.Wood.all + materials.Textile.all
    colors = [
        ["red", "crimson", "scarlet", "ruby"],
        ["orange", "ochre"],
        ["yellow", "sunshine", "gold"],
        ["green", "emerald"],
        ["blue", "cyan", "indigo", "sky", "sapphire"],
        ["violet", "purple", "fuschia", "magenta"],
        ["white", "ivory", "silver"],
        ["black", "ebony"],
    ]

    def __init__(self, *a):
        super().__init__(*a)
        self.color = choose_from(self.colors)[0]

    def as_pverb(self):
        verb = "painted"
        if self.applied_to in materials.Textile.all:
            if self.color in ["white", "ivory"]:
                verb = "bleached"
            else:
                verb = "dyed"
        elif self.applied_to in materials.Wood.all:
            verb = "stained"
        return "is {} {}".format(verb, self.color)


class Signature(Decor):
    """Signed by someone important"""

    __adj__ = "Signed"

    def __init__(self, *a, signatory=None, **kw):
        super().__init__(*a, **kw)
        self.text = signatory

    def as_pverb(self):
        o = f"has been {self.__adj__.lower()}"
        if self.text:
            o += f" by '{self.text}'"
        else:
            o += ", but the text is illegible"
        return o


class Label(Decor):
    """A small tag is attached"""

    __adj__ = "Labelled"
    removable = True

    def __init__(self, *a, text=None, **kw):
        super().__init__(*a, **kw)
        self.text = text

    def as_pverb(self):
        o = f"is {self.__adj__.lower()}"
        if self.text:
            o += f", \"{self.text}\""
        else:
            o += ", but the text is illegible"
        return o
