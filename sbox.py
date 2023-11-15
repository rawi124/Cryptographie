import tables_des as tb

def sbox(a):
    dernier = a & 1
    premier = (a >> 5) << 1
    ligne = dernier | premier
    new_a = a >> 1
    colonne = new_a & 15 
    return [ligne, colonne]

def deci_a_bin(entier):
    while entier > 0 :
        print(entier & 1)
        entier >>= 1
    
def sbox_inv(sortie, num_sbox):
    res = []
    result = 0
    i = 0
    while i < len(tb.sBox[num_sbox]):
        if tb.sBox[num_sbox][i] == sortie :
            colonne = i%16 
            ligne = i//16
            premier = ligne & 1 # bit du poids le plus faible
            dernier = (ligne >> 1) & 1 # bit du poids le plus fort
            k = 1
            while colonne > 0 :
                bit = colonne & 1
                premier = premier | (bit << k)
                k += 1
                colonne >>= 1
            premier = premier | (dernier << k)
            res.append(premier)
        i += 1
        
    return res

print(sbox_inv(3, 1))
        
        
