from .creature_core import Creature


class Human(Creature):
    race = "Human"
    race_adj = "Human"
    race_plural = "Humans"
    race_collective = "Humanity"

    sapient = True


class Elf(Creature):
    race = "Elf"
    race_adj = "Elves"
    race_plural = "Elven"
    race_collective = "Elfdom"

    sapient = True

    speed_swim = 3

    lifespan = 700
