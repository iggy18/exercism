def distance(strand_a, strand_b):
    if not len(strand_a) == len(strand_b):
        raise ValueError('strings need to be of the same length')
    if not strand_a and not strand_b:
        return 0
    hamming = 0
    for a, b in zip(strand_a, strand_b):
        if not a == b:
            hamming += 1
    return hamming