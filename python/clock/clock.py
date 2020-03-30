class Clock:
    def __init__(self, hour, minute):
        self.hour = hour % 24
        self.minute = minute
        self.fix_minutes()

    def __repr__(self):
        return f"{('00' + str(self.hour))[-2:]}:{('00' + str(self.minute))[-2:]}"

    def __eq__(self, other):
        if type(other) is not type(self):
            return False
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        self.minute += minutes
        self.fix_minutes()
        return self

    def __sub__(self, minutes):
        self.minute -= minutes
        self.fix_minutes()
        return self

    def fix_minutes(self):
        if self.minute < 0:
            while self.minute < 0:
                self.hour = (self.hour - 1) % 24
                self.minute += 60
        elif self.minute >= 60:
            while self.minute >= 60:
                self.hour = (self.hour + 1) % 24
                self.minute -= 60
