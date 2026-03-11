def SkewArray(Genome):
    skew = [0]
    for i in range(len(Genome)):
        if Genome[i] == 'G':
            skew.append(skew[i] + 1)
        elif Genome[i] == 'C':
            skew.append(skew[i] - 1)
        else:
            skew.append(skew[i])
    return skew

def MinimumSkew(Genome):
    skew = SkewArray(Genome)
    min_skew = min(skew)
    return [i for i, value in enumerate(skew) if value == min_skew] 