def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError(f'Strands must by of equal length. {len(strand_a)} != {len(strand_b)}')

    return len([(a, b) for a, b in zip(strand_a, strand_b) if a != b])
