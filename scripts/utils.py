def reverse(pattern):
    return pattern[::-1]

def Complement(pattern):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    new_patern = ""
    for i in pattern:
        if i in complement:
            new_patern += complement[i]
    return new_patern

def ReverseComplement(pattern):
    return reverse(Complement(pattern))

def HammingDistance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Las cadenas deben tener la misma longitud")
    distancia = 0
    for a, b in zip(s1, s2):
        if a != b:
            distancia += 1
    return distancia