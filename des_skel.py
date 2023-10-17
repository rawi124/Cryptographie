"""
implente le DES
"""
import tables_des as td

MASK30 = 3 << 28
MASK6 = 0x3f
MASK28 = 0xfffffff
MASK32 = 0xffffffff
K = 0x1123456789abcdef
M = 0xaaaabbbbccccdddd

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
        m_clait >>= 6
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


Ki = CalculKi(K)
#
#
# Application de la Permutation IP sur le message M
# le resultat est stocke dans tempo
#
# tempo = 0
# i = 0
# while i < 64:
#    tempo |= (((M >> (tables_des.IP[i] -1)) & 1) << i)
#      i = i + 1
#
# les 16 tours du DES
# L = (tempo >> 32)
# R = tempo & MASK32
# i = 0
# while i < 16 :
#    Z = L
#  L = R
#
#  # expansion de R via la table E
#  # resultat stocke dans tempo
#  tempo = 0
#  j = 0
#  while j < 48:
#      # A COMPLETER
#
#  # ajout de la clef de tour
#  tempo ^= Ki[i]
#
#  # action des boites S
#  tempo = S(tempo);
#
#  # Application de la permutation P sur tempo
#  # on stocke le resultat dans R
#  R = 0
#  j = 0
#  while j < 32:
#      # A COMPLETER
#  R ^= Z
#  i = i + 1
#
# echange final entre R et L
# A COMPLETER
#
# Application de la Permutation IP^-1 sur (R16L16)
# le resultat est stocke dans C
# C = 0
# i = 0
# while i < 64:
#    # A COMPLETER
# print("Crypto = ",hex(C))
#
