import re


def is_valid(isbn):
    if len(isbn) < 10:
        return False

    isbn = isbn.lower()
    digits = re.sub(r'[^0-9]', '', isbn[:-1])
    last = [int(isbn[-1])] if isbn[-1].isdigit() else [10] if isbn[-1] == 'x' else []
    digits = [int(x) for x in digits] + last
    if len(digits) != 10:
        return False
    return sum([x * (10 - i) for i, x in enumerate(digits)]) % 11 == 0
