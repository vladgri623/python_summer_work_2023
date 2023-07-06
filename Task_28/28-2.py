def hamming_distance(s1, s2):
    dst = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            dst += 1
    return dst


print(hamming_distance('abc', 'abc'))
print(hamming_distance('abc', 'abd'))
print(hamming_distance('abc', 'xyz'))
