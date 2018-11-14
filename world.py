import grammar
import dungeontime


def do_move(character, destination):
    room = character.location
    room.occupants.remove(character)
    character.location = destination
    destination.occupants.append(character)


class Room:
    def __init__(self, site, descriptor, roomtype="room", outside=False, light=0, *arg, **kw):
        self.site = site
        self.descriptor = descriptor
        self.roomtype = roomtype

        self.outside = outside
        self.light = light
            # 0: Dark
            # 1: Daylight
            # 2: Light

        self.doors = []
        self.floor = []
        self.occupants = []
        self.furniture = []

    def list_doors(self):
        out = []
        for door in self.doors:
            out.append(self.inspect(door))

    def inspect_tersely(self):
        out = " ".join([self.descriptor, self.roomtype]).strip().lower()
        return grammar.get_a(out, True)

    def inspect(self, item=None, viewer=None):
        """This is a method, not a function, so that something will always be described from the point of view of a Room"""
        if item:
            if item in self.doors:
                # Describe the door, and possibly, the room beyond
                new = item["type"]
                if item["open"]:
                    new += " On the other side you can see {}.".format(
                        item["dest"].inspect_tersely()
                    )
                    words = [
                        "items" if item["dest"].floor else None,
                        "living things" if item["dest"].occupants else None,
                    ]
                    if words:
                        new += " There are {} there.".format(
                            grammar.sequence_words(words)
                        )
            else:
                # Simply state the object name (with a/an)
                new = grammar.get_a(
                    " ".join([self.descriptor, self.roomtype]).strip().lower(), True
                )
            return new
        else:
            # Describe the room
            if not self.light or (self.light == 1 and not dungeontime.is_day()):
                return "It is quite dark."
            else:
                pass


def door_new(a: Room, b: Room, adjective="", pathtype="door"):
    if True in [True if b in door.values() else False for door in a.doors]:
        return
    new = {
        "type": pathtype,
        "dest": b,
        "open": False,
        "lock": False,
        "adjective": adjective,
    }
    a.doors.append(new)


def connect_rooms(a: Room, b: Room, *arg, **kw):
    door_new(a, b, *arg, **kw)
    door_new(b, a, *arg, **kw)


class Site:
    def __init__(self):
        self.rooms = []
        self.sites = []

    def new_room(self, *arg, **kw):
        new = Room(self, *arg, **kw)
        self.rooms.append(new)
