from collections import Counter
import re


def count_words(sentence):
    sentence = sentence.lower()
    words = re.split(r"[^a-z0-9']", sentence)
    words = [x.lstrip("'").rstrip("'") for x in words if x != '']
    return dict(Counter(words).items())
