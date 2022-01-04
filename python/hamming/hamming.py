def distance(strand_a: str, strand_b: str) -> int:
    '''
    Calculate the Hamming distance between two strings representing
    DNA strands.

    Input strings must be of equal length.

    Keyword arguments:
    strand_a, strand_b: strings representing DNA strands
    
    Returns an int representing the Hamming distance between the two strings
    '''
    if len(strand_a) != len(strand_b):
        raise ValueError("DNA strand strings must be of equal length")
    if len(strand_a) == 0:
        return 0
    else:
        if strand_a[0] != strand_b[0]:
            return 1 + distance(strand_a[1:], strand_b[1:])
        else: return distance(strand_a[1:], strand_b[1:])
