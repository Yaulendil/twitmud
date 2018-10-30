"""
Weapon Parts that do not contribute damage. Handles, guards, etc.
"""
from items import materials
from treasure_core import TreasureObject, form_out


class WPart(TreasureObject):
    traits = {"Material": materials.Metal.weapons}
    TreasureType = "Weapon Component"
    baseDurability = 5

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        # Base values; Multiplied later
        self.Size = (
            1
        )  # Approximate volume occupied by the component; Affects reach and weight
        self.HP = (
            self.baseDurability * self.mat_stat["Toughness"]
        )  # "Health" of a part determines when it breaks and what its damage adjective is

    @property
    def mat_stat(self):
        test = self.traits["Material"]
        if type(test) == tuple:
            test = test[0]
        test = test[self.dictTrait["Material"]]  # Get the base stat table
        return test
        # noinspection PyUnreachableCode
        """
        {"Value":10, # Monetary worth of the material
         "Density":10, # How much mass is in a given volume; Weapon weight
         "Hardness":10, # How well a weapon maintains shape; Aids sharpness
         "Toughness":10, # Difficulty to permanently deform; Durability
         "Flexibility":10}, # Ability to temporarily deform
        """

    def damage_rating(
        self, split=True
    ):  # Amount of damage contributed by this component
        d = []
        try:
            d_base = self.mat_stat  # Damage bases
            d_scale = self.map_damage  # Damage scale factors
            # DB(self, d_base, d_scale)
            for (
                n
            ) in d_scale:  # Do the following for EACH STAT and then add it to the list
                # DB(n, d_scale[n], d)
                d.append(
                    float(
                        d_scale[n]  # wp.mapDamage["Density"] (0.5)
                        * d_base[n]  # MULTIPLIED by d_base["Density"] (10)
                        * self.base_damage
                    )
                )  # AND by base damage of the component class
        except Exception as e:
            d = [0, 0, 0]
            # DB(e)
        for i in range(len(d)):
            try:  # d[i] should be a matching damage type...
                assert i in self.damage_types
            except:  # ...Otherwise, make it relatively bad
                d[i] /= 4
        return [round(i, 2) for i in d]

    def describe(self, solo=True, pad="", full=False):
        o = super().describe(solo, pad, full)
        d = self.damage_rating()
        if sum(d) > 0:
            o += form_out(f"It contributes {d} C/P/S damage.", pad, True)
        return o
