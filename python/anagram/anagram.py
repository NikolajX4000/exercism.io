from collections import Counter


def find_anagrams(word, candidates):
    word_counter = Counter(word.lower())
    return [c for c in candidates if word_counter == Counter(c.lower()) and word.lower() != c.lower()]
