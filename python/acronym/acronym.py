import re


def abbreviate(words):
    words = re.split("[^A-Z']", words.upper())
    return ''.join([x[0] for x in words if x != ''])