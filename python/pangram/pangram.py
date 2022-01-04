import string

def is_pangram(sentence: str) -> bool:
    '''
    Determines whether input sentence is a pangram (i.e. contains every letter in the
    alphabet at least once)

    Keyword arguments:
        sentence: string to test

    Returns true if input sentence is a pangram and false otherwise
    '''
    
    # Select lowercase ascii letters
    letters = list(string.ascii_letters[:26])

    # Remove character from letters list if character is in list, otherwise continue
    for char in sentence:
        try:
            letters.remove(char.lower())
        except ValueError:
            continue
    
    if letters: return False
    else: return True
