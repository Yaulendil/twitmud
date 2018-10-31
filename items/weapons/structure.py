"""
Weapon Parts that do not contribute damage. Handles, guards, etc.
"""
from items import materials
from items.treasure_core import TreasureObject, form_out


class WPart(TreasureObject):
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

    @property
    def material(self):
        # try:
        material = self.dictTrait["Material"]
        while type(material) in [tuple, list, dict]:
            material = material[0]
        # except:
        #     material = None
        return material

    def damage_rating(self, split=True):
        # Amount of damage contributed by this component
        d = []
        try:  # FC: Assume the part contributes damage
            # d_base = self.material  # Damage bases
            # d_scale = self.stat_damage  # Damage scale factors
            # for n in d_scale:
            #     # Do the following for EACH STAT and then add it to the list
            #     d.append(
            #         float(
            #             d_scale[n]  # wp.mapDamage["Density"] (0.5)
            #             * d_base[n]  # MULTIPLIED by d_base["Density"] (10)
            #             * self.base_damage  # AND by base damage of the component class
            #         )
            #     )

            for damage_type, coeffs in self.type_damage.items():
                damage = 0
                # for damage_stat, coeff in self.stat_damage.items():
                for damage_stat, coeff in coeffs.items():
                    damage += getattr(self.material, damage_stat) * coeff
                d.append(damage)

            for i in range(len(d)):
                if i in self.DamageTypesGood:
                    d[i] *= self.Effectiveness
        except:  # FC: It has been found that this part contributes no damage
            d = [0, 0, 0]
        return [round(i, 2) for i in d]

    def describe(self, solo=True, pad="", full=False):
        o = super().describe(solo, pad, full)
        d = self.damage_rating()
        if sum(d) > 0:
            o += form_out(f"It contributes {d} C/P/S damage.", pad, True)
        return o
