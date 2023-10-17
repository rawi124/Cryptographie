def sbox(a):
    dernier = a & 1
    premier = (a >> 5) << 1
    ligne = dernier | premier
    new_a = a >> 1
    print(new_a)
    colonne = new_a ^ (1 << 4) 
    return [ligne, colonne]
print(sbox(10))
