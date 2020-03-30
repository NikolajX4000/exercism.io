"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Score categories.
# Change the values as you see fit.

YACHT = (lambda x: 50 if len(set(x)) == 1 else 0)
ONES = lambda d: sum(x for x in d if x == 1)
TWOS = lambda d: sum(x for x in d if x == 2)
THREES = lambda d: sum(x for x in d if x == 3)
FOURS = lambda d: sum(x for x in d if x == 4)
FIVES = lambda d: sum(x for x in d if x == 5)
SIXES = lambda d: sum(x for x in d if x == 6)
FULL_HOUSE = lambda d: sum(d) if len(set(d)) == 2 and any(d.count(x) == 3 for x in set(d)) else 0
FOUR_OF_A_KIND = lambda d: sum(x * 4 for x in set(d) if d.count(x) > 3)
LITTLE_STRAIGHT = (lambda x: 30 if sorted(x) == [1, 2, 3, 4, 5] else 0)
BIG_STRAIGHT = (lambda x: 30 if sorted(x) == [2, 3, 4, 5, 6] else 0)
CHOICE = sum


def score(dice, category):
    if any(not 0 < x < 7 for x in dice):
        raise ValueError("Invalid dice {}".format(dice))
    return category(dice)
