import jsonpickle

import random
from numpy import add as npadd

from items.treasure_core import TreasureObject
import items


def load(fname):
    with open(fname, "r") as fh:
        data = fh.read()
    item = jsonpickle.decode(data)
    return item


def asdf(qwert, full=False):
    print(qwert().describe(solo=True, full=full))
