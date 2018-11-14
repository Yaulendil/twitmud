import datetime as dt

from astral import Astral


A = Astral()
L = A["London"]
ZERO = dt.timedelta(0)


class UTC(dt.tzinfo):
    def utcoffset(self, _):
      return ZERO

    def tzname(self, _):
      return "UTC"

    def dst(self, _):
      return ZERO


utc = UTC()


def now():
    return dt.datetime.now(utc)


def is_day():
    return L.dawn() < now() < L.night()[0]
