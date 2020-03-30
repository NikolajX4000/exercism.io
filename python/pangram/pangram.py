import re


def is_pangram(sentence):
    letters = set(re.sub(r'[^a-z]', '', sentence.lower()))
    return set('abcdefghijklmnopqrstuvwxyz') == letters
