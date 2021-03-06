TRANSITIONS = [
    ['0000', '0000', lambda p, pi1, pi2: p],
    ['0000', '0100', lambda p, pi1, pi2: not p],
    ['0001', '0001', lambda p, pi1, pi2: p and pi2],
    ['0001', '0000', lambda p, pi1, pi2: (not pi2) and p],
    ['0001', '0101', lambda p, pi1, pi2: (not p) and pi2],
    ['0001', '0100', lambda p, pi1, pi2: (not pi2) and (not p)],
    ['0011', '0101', lambda p, pi1, pi2: (not p) and (not pi2)],
    ['0011', '0001', lambda p, pi1, pi2: p and (not pi2)],
    ['0011', '0111', lambda p, pi1, pi2: (not p) and pi2],
    ['0011', '0011', lambda p, pi1, pi2: p and pi2],
    ['0100', '0100', lambda p, pi1, pi2: pi1 and p],
    ['0100', '1100', lambda p, pi1, pi2: pi1 and (not p)],
    ['0100', '0001', lambda p, pi1, pi2: (not pi1) and p],
    ['0100', '0101', lambda p, pi1, pi2: (not p) and (not pi1)],
    ['0101', '0101', lambda p, pi1, pi2: pi1 and pi2 and p],
    ['0101', '0101', lambda p, pi1, pi2: (not pi1) and (not pi2) and (not p)],
    ['0101', '0100', lambda p, pi1, pi2: p and pi1 and (not pi2)],
    ['0101', '1101', lambda p, pi1, pi2: pi1 and pi2 and (not p)],
    ['0101', '0001', lambda p, pi1, pi2: (not pi1) and (not pi2) and p],
    ['0101', '0011', lambda p, pi1, pi2: (not pi1) and pi2 and p],
    ['0101', '0111', lambda p, pi1, pi2: (not pi1) and pi2 and (not p)],
    ['0101', '1100', lambda p, pi1, pi2: (not p) and pi1 and (not pi2)],
    ['0111', '0111', lambda p, pi1, pi2: (not p) and (not pi1)],
    ['0111', '0111', lambda p, pi1, pi2: p and pi1 and pi2],
    ['0111', '0101', lambda p, pi1, pi2: p and pi1 and (not pi2)],
    ['0111', '0011', lambda p, pi1, pi2: p and (not pi1)],
    ['0111', '1111', lambda p, pi1, pi2: (not p) and pi1 and pi2],
    ['0111', '1101', lambda p, pi1, pi2: (not p) and pi1 and (not pi2)],
    ['1100', '1100', lambda p, pi1, pi2: pi1],
    ['1100', '0101', lambda p, pi1, pi2: (not pi1)],
    ['1101', '1100', lambda p, pi1, pi2: pi1 and (not pi2)],
    ['1101', '1101', lambda p, pi1, pi2: pi1 and pi2],
    ['1101', '0100', lambda p, pi1, pi2: (not pi1) and (not pi2)],
    ['1101', '0111', lambda p, pi1, pi2: (not pi1) and pi2],
    ['1111', '1111', lambda p, pi1, pi2: pi1 and pi2],
    ['1111', '1101', lambda p, pi1, pi2: pi1 and (not pi2)],
    ['1111', '0111', lambda p, pi1, pi2: (not pi1)],
]