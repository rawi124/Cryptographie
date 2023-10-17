"""
implente le DES
"""
import tables_des as td

MASK30 = 3 << 28
MASK6 = 0x3f
MASK28 = 0xfffffff
MASK32 = 0xffffffff

def sbox(n, a):
    """
    retourne la valeur de la ligne et la colonne de la SBOX
    correpondante a a
    """
    dernier = a & 1
    premier = (a >> 5) << 1
    ligne = dernier | premier
    new_a = a >> 1
    colonne = new_a & 15
    position = ligne * 16 + colonne
    return td.sBox[n][position]


def S(m_clair):
    """
    retourne la boite S 
    """
    result = 0
    i = 0
    while i < 8:
        mot = m_clair & 63
        sortie = sbox(i, mot)
        m_clair >>= 6
        tmp = result
        result = sortie << (4*i) | tmp
        i += 1
    return result


def CalculKi(cle):
    """
    genere les 16 cles intermidiaires
    """
    PC1K = 0
    cle_i = [0]*16
    i = 0
    while i < 56:
        b = td.PC1[i]-1
        bit = (cle >> b) & 1
        tmp = PC1K
        PC1K = tmp | (bit << i)
        i += 1
    gauche = (PC1K >> 28) & MASK28
    droite = PC1K & MASK28
    i = 0
    while i < 16:
        bit_shift = td.LS[i]
        gauche = ((gauche << bit_shift) & MASK28) | (gauche >> (28 - bit_shift))
        droite = ((droite << bit_shift) & MASK28) | (droite >> (28 - bit_shift))
        tempo = (gauche << 28) | droite
        cle_i[i] = 0
        j = 0
        ki = 0
        while j < 48:
            b = td.PC2[j] -1 
            bit = (tempo >> b) & 1
            tmp = ki
            ki = tmp | (bit <<j )
            j += 1
        cle_i[i] = ki
        i += 1
    return (cle_i)

def DES(M, cle):
    """
    effectue le standard DES
    """
    tempo = 0
    i = 0
    while i < 64:
        tempo |= (((M >> (td.IP[i] -1)) & 1) << i)
        i = i + 1
    L = (tempo >> 32)
    R = tempo & MASK32
    i = 0
    while i < 16 :
        print(hex(L), hex(R))
        Z = L
        L = R
        tempo = 0
        j = 0
        while j < 48:
            b = td.E[j] -1
            bit = (R >> b) & 1
            tmp = tempo
            tempo = tmp | (bit << j)
            j += 1
        print("e ", hex(tempo))
        tempo ^= cle[i]
        print("xor cle ", hex(tempo), " cle", hex(cle[i]))
        tempo = S(tempo)
        print("s ", hex(tempo))
        
        R = 0
        j = 0
        while j < 32:
            b = td.P[j] - 1
            bit = (tempo >> b) & 1
            tmp = R
            R = tmp | (bit << j)
            j += 1
        R ^= Z
        print("################################################################################")
        i = i + 1
    print("ici",hex(L), hex(R))
    L, R = R, L
    O = 0
    i = 0
    print("ici",hex(L), hex(R))
    nv_bloc = (R << 32) | L
    while i < 64:
        O |= (((nv_bloc >> (td.InvIP[i] -1)) & 1) << i)
        i = i + 1
    return hex(O)
if __name__ == "__main__":
    K = 0x1123456789abcdef
    M = 0xaaaabbbbccccdddd
    Ki = CalculKi(K)
    print(DES(M, Ki))

