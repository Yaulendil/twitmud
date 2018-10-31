"""
Weapon Parts that do not contribute damage. Handles, guards, etc.
"""
from items import materials
from items.treasure_core import TreasureObject
from grammar import form_out


class WPart(TreasureObject):
    size = 10
    traits = {"Material": materials.Metal.decor + materials.Metal.structure}
    TreasureType = "Tool Component"
    base_durability = 5

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        # Base values; Multiplied later
        # self.size = 1
        # # Approximate volume occupied by the component; Affects reach and weight
        self.hp = self.base_durability * self.material.Toughness
        # "Health" of a part determines when it breaks and what its damage adjective is

    def damage_rating(self, split=True):
        # Amount of damage contributed by this component
        return [0, 0, 0] if split else 0

    def describe(self, solo=True, pad="", full=False):
        o = super().describe(solo, pad, full)
        d = self.damage_rating()
        dstr = [str(n) for n in d]
        if sum(d) > 0:
            o += form_out(f"It contributes {dstr} C/P/S damage.", pad, True)
        return o


class Grip(WPart):
    size = 0.5
    traits = {"Material": materials.Textile.all}
    TreasureType = "simple wrapping"


class GripWide(WPart):
    size = 1.5
    traits = {"Material": materials.Textile.all}
    TreasureType = "long wrapping"


class Handle(WPart):
    size = 3
    traits = {"Material": materials.Metal.structure + materials.Wood.structure}
    components = {"Grip": [None, Grip]}
    TreasureType = "straight handle"


class HandleLong(WPart):
    size = 8
    traits = {"Material": materials.Metal.structure + materials.Wood.structure}
    components = {"Grip": [None, GripWide]}
    TreasureType = "long handle"


class HandleLonger(WPart):
    size = 14
    traits = {"Material": materials.Metal.structure + materials.Wood.structure}
    components = {"Upper Grip": [None, Grip, GripWide],
                  "Lower Grip": [None, Grip, GripWide]}
    TreasureType = "pole"


class Crossguard(WPart):
    size = 4
    TreasureType = "crossguard"


class Roundguard(WPart):
    size = 2
    TreasureType = "round guard"


class Basket(WPart):
    size = 3
    TreasureType = "basket guard"
