from re import sub


def encode(string):
    return sub(r'(.)\1+', lambda x: str(len(x.group(0))) + x.group(0)[0], string)


def decode(string):
    return sub(r'(\d+)(\D)', lambda x: x.group(2) * int(x.group(1)), string)
