import string

def is_isogram(seq: str) -> bool:
    '''
    Determines whether input string is an isogram (a sequence of characters
    with no reoccuring characters)

    Keyword arguments:
        string: the sequence of characters to test

    Returns a boolean value of true if the string is an isogram and false otherwise
    '''
    chars_seen = []

    for char in seq:
        if char in string.ascii_letters:
            if char.lower() in chars_seen: return False
            chars_seen.append(char.lower())
    return True
