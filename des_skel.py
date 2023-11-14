"""
implente le DES
qui est un algorithme de chiffrement symetrique chiffrant par bloc de 64 bits.
la cle est de longeur 56 bits ( 2**56 possibilites de cle)
grace a cette cle, on genere 16 autres intermidiaires, chacune est utilisé pour
chiffrer un bloc de donnee lors de chaque tour
un tour = permutation + subsititution(sBox)
"""
import tables_des as td

MASK30 = 3 << 28
MASK6 = 0x3f
MASK28 = 0xfffffff
MASK32 = 0xffffffff


def sbox(nb_sbox, entier):
    """
    retourne la valeur de la ligne et la colonne de la SBOX
    nb_sbox correpondante a l entier en entree
    """
    dernier = entier & 1
    premier = (entier >> 5) << 1
    ligne = dernier | premier
    new_e = entier >> 1
    colonne = new_e & 15
    position = ligne * 16 + colonne
    return td.sBox[nb_sbox][position]


def boite(m_clair):
    """
    effectue la boite S
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


def permutation(longeur, entree, table):
    """
    effectue une permutation d un mot entree selon
    une certaine table
    """
    i = 0
    sortie = 0
    while i < longeur:
        bit = (entree >> (table[i] - 1)) & 1
        sortie = sortie | (bit << i)
        i += 1
    return sortie


def calcul_ki(cle):
    """
    genere les 16 cles intermidiaires
    """
    permut_cle = permutation(56, cle, td.PC1)
    gauche = (permut_cle >> 28) & MASK28
    droite = permut_cle & MASK28
    cle_i = [0] * 16
    i = 0
    while i < 16:
        bit_shift = td.LS[i]
        gauche = ((gauche << bit_shift) & MASK28) | (
            gauche >> (28 - bit_shift))
        droite = ((droite << bit_shift) & MASK28) | (
            droite >> (28 - bit_shift))
        tempo = (gauche << 28) | droite
        cle_i[i] = permutation(48, tempo, td.PC2)
        i += 1
    return cle_i


def standard_des(mot, cle,crypt=True):
    """
    effectue le standard DES
    """
    tempo = permutation(64, mot, td.IP)
    left = (tempo >> 32) 
    right = tempo & MASK32
    i = 0
    while i < 16:
        tmp = left
        left = right
        tempo = permutation(48, right, td.E)
        tempo ^= cle[i] if crypt else cle[15-i]
        tempo = boite(tempo)
        right = permutation(32, tempo, td.P)
        right ^= tmp
        i = i + 1
    nv_bloc = (right << 32) | left
    return permutation(64, nv_bloc, td.InvIP)

def decrypt(mot, cle):
    """
    effectue le decrypt du standard DES
    """
    tempo = permutation(64, mot, td.IP)
    left = (tempo >> 32)
    right = tempo & MASK32
    i = 15
    while i >= 0 :
        tmp = left
        left = right
        tempo = permutation(48, right, td.E)
        tempo ^= cle[i]
        tempo = boite(tempo)
        right = permutation(32, tempo, td.P)
        right ^= tmp
        i = i - 1
    nv_bloc = (right << 32) | left
    return hex(permutation(64, nv_bloc, td.InvIP))



if __name__ == "__main__":
    K = 0x1123456789abcdef
    M = 0xaaaabbbbccccdddd
    cles = calcul_ki(K)
    print(decrypt(standard_des(M, cles), cles))
