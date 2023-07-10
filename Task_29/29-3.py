def is_iso(s1, s2):
    if len(s1) != len(s2): return False
    if len(set(s1)) != len(set(s2)): return False

    pairs = list()
    for i in range(len(s1)):
        if (s1[i], s2[i]) in pairs:
            continue
        else: pairs.append((s1[i], s2[i]))
    for i in pairs:
        l1, c = i[0], 0
        for j in pairs:
            if (j[0] == l1) and (j != i):
                return False
    return True


print(is_iso('CBAABC', 'DEFFED'))
print(is_iso('XXX', 'YYY'))
print(is_iso('RAMBUNCTIOUSLY', 'THERMODYNAMICS'))
print(is_iso('AB', 'CC'))
print(is_iso('XXY', 'XYY'))
print(is_iso('ABAB', 'CD'))
