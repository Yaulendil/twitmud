"""
MATERIALS provide the BASE VALUE of an object, as well as its stats.
An object can be made from any material which has all the required stats for the object type.
"""

METAL = {"Iron":{ # "Standard" metal, quite balanced
             "Value":10, # Monetary worth of the material
             "Density":10, # How much mass is in a given volume; Weapon weight
             "Hardness":10, # How well a weapon maintains shape; Aids sharpness
             "Toughness":10, # Difficulty to permanently deform; Durability
             "Flexibility":10}, # Ability to temporarily deform
         "Steel":{ # Alloyed iron, generally better but more brittle
             "Value":14,
             "Density":10,
             "Hardness":10,
             "Toughness":10,
             "Flexibility":10},
         "Brass":{ # An aesthetically pleasant alloy; Not particularly exceptional
             "Value":12,
             "Density":10,
             "Hardness":10,
             "Toughness":10,
             "Flexibility":10},
         "Bronze":{ # A weapons-grade alloy of cheaper metals
             "Value":8,
             "Density":10,
             "Hardness":10,
             "Toughness":10,
             "Flexibility":10},
         "Copper":{ # A cheap metal, easily outclassed
             "Value":6,
             "Density":8,
             "Hardness":10,
             "Toughness":10,
             "Flexibility":10},
         "Silver":{ # Precious metal, soft but rather heavy
             "Value":16,
             "Density":15,
             "Hardness":7,
             "Toughness":10,
             "Flexibility":10},
         "Gold":{ # Very precious metal, quite soft but very heavy
             "Value":18,
             "Density":18,
             "Hardness":5,
             "Toughness":10,
             "Flexibility":10
             },
         "Mithril":{ # Legendary metal, unnaturally light and sharp
             "Value":24,
             "Density":6,
             "Hardness":10,
             "Toughness":10,
             "Flexibility":10
             },
         "Adamantium":{ # Legendary metal, unnaturally hard and heavy
             "Value":24,
             "Density":22,
             "Hardness":10,
             "Toughness":10,
             "Flexibility":10
             }}

WOOD = {}

GEMSTONE = {}

TEXTILE = {}

GLASS = {"Glass":{
             "Value":3},
         "Crystal":{
             "Value":7}}




