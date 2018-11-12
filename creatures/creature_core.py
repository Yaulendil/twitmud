STATUS_STATE = ["Healthy", "Injured", "Wounded", "Critical"]
STATUS_RECOVERY = [0, 8, 24, 72]


class BodyPart:
    def __init__(self):
        self.hp = 100
        self.dead = False

    def damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            self.dead = True


class Creature:
    """Any living thing. Human, cat, turtle, goblin, tree, flower...."""

    ### Body Map: Critical inventory of a creature
    ### All parts are assumed to be adjacent to a Vital
    # Vital: Body parts without which the creature would die
    vital = ["Torso", "Head"]
    # Movement: Body parts used for various movement types
    walk = ["Right Leg", "Left Leg"]
    swim = ["Right Leg", "Left Leg", "Right Arm", "Left Arm"]
    fly = []
    # Grasp: Body parts used for picking things up
    grasp = ["Right Arm", "Left Arm"]
    # Aux: Body parts not critical to any operations
    aux = []

    race = "Creature"
    race_adj = "Created"
    race_plural = "Creatures"
    race_collective = "Creation"

    sentient = True  # Capable of feeling. Not plants or fungi.
    sapient = False  # Capable of conscious thought. "People".

    speed_walk = 10  # Base movement speed on land.
    speed_swim = 4  # Base movement speed in water.
    speed_fly = 0  # Base movement speed through the air.

    rate_healing = 10
    lifespan = 70

    def __init__(self, name=None, location=None, status=0):
        self.name = name
        self.body = {}
        for slot in set(
            self.vital + self.walk + self.swim + self.fly + self.grasp + self.aux
        ):
            self.body[slot] = BodyPart()

        self.location = location
        self.status = status

        self.skill_walk = 1
        self.skill_swim = 1
        self.skill_fly = 1

    def speed(self, stype):
        speed = getattr(self, "speed_" + stype, 0)
        skill = getattr(self, "skill_" + stype, 0)
        return speed * skill
