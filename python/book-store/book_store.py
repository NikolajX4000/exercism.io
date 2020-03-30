import math
from collections import Counter
from functools import reduce

PER_BOOK = 800.00
PER_GROUP = {1: 1 * PER_BOOK * 1, 2: 2 * PER_BOOK * 0.95, 3: 3 * PER_BOOK * 0.90, 4: 4 * PER_BOOK * 0.80,
             5: 5 * PER_BOOK * 0.75}


def _recursive_total(books):
    volumes = Counter(books)
    num_books, num_volumes = len(books), len(volumes)

    if num_volumes == 1:
        return num_books * PER_BOOK

    if num_books == num_volumes:
        return PER_GROUP[num_books]

    gcd = reduce(math.gcd, volumes.values())
    if gcd != 1:
        minimal = Counter({k: v // gcd for k, v in volumes.items()})
        minimal_books = tuple(sorted(minimal.elements()))
        return _recursive_total(minimal_books) * gcd

    price = num_books * PER_BOOK
    for num in range(num_volumes, 1, -1):
        group = volumes - Counter(k for k, _ in volumes.most_common(num))
        group_books = tuple(sorted(group.elements()))
        price = min(price, PER_GROUP[num] + _recursive_total(group_books))
    return price


def total(basket):
    if not basket:
        return 0
    return _recursive_total(tuple(sorted(basket)))
