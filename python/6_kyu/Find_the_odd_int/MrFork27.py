def find_it(seq):
    return list(filter(lambda n: seq.count(n) % 2 != 0, seq))[0]
