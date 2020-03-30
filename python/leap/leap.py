def leap_year(year):
    return year % 4 == 0 if year % 100 != 0 else year % 4 == 0 if year % 400 == 0 else False
