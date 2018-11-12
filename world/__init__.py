import grammar


def door_new(a, b, adjective="", pathtype="door"):
    if True in [True if b in door else False for door in a.doors.values()]:
        return
    new = {
        "type": pathtype,
        "dest": b,
        "open": False,
        "locked": False,
        "adjective": adjective,
    }


def connect_rooms(a, b, *arg, **kw):
    door_new(a, b, *arg, **kw)
    door_new(b, a, *arg, **kw)


class Room:
    def __init__(self, descriptor, *arg, **kw):
        self.descriptor = descriptor
        self.doors = []
        self.floor = []
        self.occupants = []
        self.furniture = []

    def list_doors(self):
        out = []
        for door in self.doors:
            out.append(self.inspect(door))

    def inspect(self, item=None):
        if item in self.doors:
            new = item["type"]
        elif item:
            # TODO: Simply state the object name (with a/an)
            pass
        else:
            # TODO: Describe the room
            pass


class Site:
    def __init__(self):
        self.rooms = []
        self.sites = []

    def new_room(self, *arg, **kw):
        new = Room(*arg, **kw)
