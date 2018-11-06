import jsonpickle

from . import weapons
from . import consumables
from . import decor
from . import materials
from . import treasure_core
from . import util


def load(fname):
    with open(fname, "r") as fh:
        data = fh.read()
    item = jsonpickle.decode(data)
    return item
