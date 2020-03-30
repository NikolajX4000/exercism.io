from calendar import Calendar


class MeetupDayException(ValueError):
    pass


WEEKDAYS = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
OFFSETS = {"1st": 0, "2nd": 1, "3rd": 2, "4th": 3, "5th": 4, "last": -1}


def meetup(year, month, week, day_of_week):
    weekday = WEEKDAYS[day_of_week]
    current_month = Calendar().itermonthdates(year, month)
    dates = [d for d in current_month if d.weekday() == weekday and d.month == month]
    if week == "teenth":
        return next(filter(lambda d: 12 < d.day < 20, dates))
    else:
        offset = OFFSETS[week]
        if offset < len(dates):
            return dates[offset]
        else:
            raise MeetupDayException("Invalid date")
