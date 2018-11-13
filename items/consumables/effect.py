import datetime as dt


def smaller(a, b):
    return a if a <= b else b


class Effect:
    verb = "is experiencing effects"

    time_mult = 1
    time_max = 1000

    def __init__(self, subject, duration, interval=0, strength=1):
        self.time_start = dt.datetime.now()
        self.tick_last = self.time_start
        self._duration = smaller(self.time_max, duration or 1000) * self.time_mult
        self._interval = interval or self._duration / 5

        self.strength = strength

        self.subject = subject
        subject.effects.append(self)
        self.applied()

    @property
    def duration(self):
        return dt.timedelta(hours=self._duration)

    @property
    def interval(self):
        return dt.timedelta(hours=self._interval)

    @property
    def time_end(self):
        return self.time_start + self.duration

    def ticks_due(self, since=None, to=None):
        last = since or self.tick_last
        now = to or dt.datetime.now()
        ticks = 0
        while last + (self.interval * (ticks + 1)) < smaller(now, self.time_end):
            ticks += 1
        return ticks

    def do_ticks(self):
        last = self.tick_last
        now = dt.datetime.now()
        ticks = self.ticks_due(last, now)
        for i in range(ticks):
            self.tick()
        if now > self.time_end:
            self.dispersed()
            self.subject.effects.remove(self)
        self.tick_last = now

    # Following methods are to be overwritten to actually do things

    def applied(self):
        """Called when the Effect is first applied"""
        pass

    def dispersed(self):
        """Called when the Effect expires"""
        pass

    def tick(self):
        """Called for each time an Interval passes (in clusters)"""
        pass
