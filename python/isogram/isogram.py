def is_isogram(string):
    used = []
    string = string.lower()
    for s in string:
        if s in used and ord('a') <= ord(s) <= ord('z'):
            return False
        used.append(s)
    return True
