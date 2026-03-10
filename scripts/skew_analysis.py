def SkewArray(Genome):
    skew = [0]
    for i in range(len(Genome)):
        if Genome[i] == 'C':
            skew.append(skew[-1] - 1)
        elif Genome[i] == 'G':
            skew.append(skew[-1] + 1)
        else:
            skew.append(skew[-1])
    return skew

def MinimumSkew(Genome):
    positions = []
    skew = SkewArray(Genome)
    min_skew = min(skew)
    for i in range(len(skew)):
        if skew[i] == min_skew:
            positions.append(i)
    return positions