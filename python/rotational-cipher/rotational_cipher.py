def rotate(text, key):
    UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
    return text.translate(
        str.maketrans(UPPERCASE + LOWERCASE, UPPERCASE[key:] + UPPERCASE[:key] + LOWERCASE[key:] + LOWERCASE[:key]))
