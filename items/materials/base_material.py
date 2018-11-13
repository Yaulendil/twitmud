class Material:
    Value = 100
    Rarity = 100
    Density = 100
    Hardness = 100
    Toughness = 100
    Flexibility = 100
    # Damage FX; Adjectives applied when item is damaged
    dmg_FX = {
        "phys": ["damaged", "broken"],
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
    __adj__ = "Physical"

    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return self.__name__.lower()

    all = []  # A list of all materials of this type

    common = []  # Materials which are inexpensive
    fine = []  # Materials of luxury, for the rich
    rare = []  # Materials which are very expensive

    weapons = []  # Materials considered to be weapons-grade
    decor = []  # Materials which are pretty
    structure = []  # Materials which are strong
