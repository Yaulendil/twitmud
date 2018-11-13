"""
DECOR is a stylistic modifier that adds MULTIPLIED VALUE of a material.
An example: Woven leather strips, due to the necessary labor increase, make a tool handle far more luxurious than a crude leather wrapping.
Decor has no impact on stats.
"""
from selection import choose_from
from items import materials


class Decor:
    value_add = 1
    __adj__ = "Decorated"
    materials = []
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


class MetalInlay(Decor):
    value_add = 3
    __adj__ = "Inlaid"
    materials = materials.Metal.decor


class MetalPlating(Decor):
    value_add = 2.5
    __adj__ = "Plated"
    materials = materials.Metal.decor


class GemEncrust(Decor):
    value_add = 5
    __adj__ = "Encrusted"
    materials = materials.Gemstone.all


class Carved(Decor):
    value_add = 1.5
    __adj__ = "Intricately Carved"
    material_restrict = materials.Wood.all


class Woven(Decor):
    value_add = 1.5
    __adj__ = "Finely Woven"
    material_restrict = materials.Textile.all


class Color(Decor):
    value_add = 1
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
    __adj__ = "Signed"
