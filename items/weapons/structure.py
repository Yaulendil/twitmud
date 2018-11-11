"""
Weapon Parts that do not contribute damage. Handles, guards, etc.
"""

from items import materials, decor
from items.treasure_core import TreasureObject


class WPart(TreasureObject):
    image = []
    size = 10
    # traits = {"Material": materials.Metal.decor + materials.Metal.structure}
    materials = materials.Metal.decor + materials.Metal.structure
    TreasureType = "Tool Component"
    base_durability = 5

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.hp = self.base_durability * self.material.Toughness
        # "Health" of a part determines when it breaks and what its damage adjective is

    def damage_rating(self, split=True):
        # Amount of damage contributed by this component
        return [0, 0, 0] if split else 0


class Grip(WPart):
    additions = [([None, decor.Woven], [5, 1]), [None, decor.Color]]
    size = 0.5
    materials = materials.Textile.common
    TreasureType = "simple wrapping"


class GripWide(Grip):
    size = 1.5
    TreasureType = "long wrapping"


class Handle(WPart):
    image = [
        "   ┃   ",
        "   ┃   ",
    ]

    additions = [([None, decor.Carved], [5, 1]), [None, decor.Color]]
    size = 3
    materials = materials.Metal.structure + materials.Wood.structure
    components = {"Grip": [None, Grip]}
    TreasureType = "straight handle"


class HandleLong(Handle):
    image = [
        "   ┃   ",
        "   ┃   ",
        "   ┃   ",
        "   ┃   ",
        "   ┃   ",
    ]

    size = 8
    components = {"Grip": [None, GripWide]}
    TreasureType = "long handle"


class HandleLonger(Handle):
    image = [
        "   ┃   ",
        "   ┃   ",
        "   ┃   ",
        "   ┃   ",
        "   ┃   ",
        "   ┃   ",
        "   ┃   ",
        "   ┃   ",
        "   ┃   ",
        "   ┃   ",
        "   ┃   ",
    ]

    size = 14
    components = {
        "Upper Grip": [None, Grip, GripWide],
        "Lower Grip": [None, Grip, GripWide],
    }
    TreasureType = "pole"


class Crossguard(WPart):
    image = [
        "▜█████▛",
    ]

    size = 4
    additions = [([None, decor.GemEncrust, decor.MetalInlay], [10, 1, 5])]
    TreasureType = "crossguard"


class Roundguard(WPart):
    image = [
        " ▟███▙ ",
    ]

    size = 2
    additions = [([None, decor.GemEncrust, decor.MetalInlay], [10, 1, 5])]
    TreasureType = "round guard"


class Basket(WPart):
    image = [
        " ▟███▙ ",
        " █████ ",
    ]

    size = 3
    additions = [([None, decor.GemEncrust, decor.MetalInlay], [10, 1, 5])]
    TreasureType = "basket guard"
