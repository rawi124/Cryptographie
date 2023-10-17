"""
implente le DES
"""
import tables_des as td

def sbox(n,a):
    """
    retourne la ligne et la colonne de
    la SBOX
    """
    dernier = a & 1
    premier = (a >> 5) << 1
    ligne = dernier | premier
    new_a = a >> 1
    colonne = new_a & 15
    position = ligne * 16 + colonne
    return td.sBox[n][position]


def S(x):
    """
    retourne la boite S 
    """
    result = 0
    i = 0 
    while i < 8:
        mot = x & 63
        sortie = sbox(i, mot)
        x = x >> 6
        tmp = result
        result = sortie << (4*i) | tmp
        i += 1
    return result

def CalculKi(K):
    #attention C et D doivent etre consideres stockes que sur 28 bits 
    PC1K = 0
    ki = [0]*16
    i = 0 
    while (i < 56):
        # A COMPLETER
        b = td.PC1[i]-1
        bit = (K >> b) & 1
        tmp = PC1K
        PC1K = tmp| ( bit << i )
        i += 1
    C = (PC1K >> 28) & MASK28 
    D = PC1K & MASK28 ;
    i = 0
    while (i < 16):
        bit_shift = td.LS[i]
        aa = (C << bit_shift)
        tmp = (aa & MASK30) >> 28
        C = (aa | tmp) & MASK28
        tempo = (C << 28) | D;
        ki[i] = 0;
        j = 0
        # Application de la permutation PC2 sur tempo afin d'obtenir la cle de tour numero 
        # le resultat est stocke dans ki[i]
        while (j < 48):
            # A COMPLETER
            j += 1
        i += 1

    return(ki)
#
MASK30 = 3 << 28
MASK6 = 0x3f
MASK28 = 0xfffffff
MASK32 = 0xffffffff
K=0x1123456789abcdef
M=0xaaaabbbbccccdddd
#
Ki = CalculKi(K)
#
#
##Application de la Permutation IP sur le message M 
## le resultat est stocke dans tempo
#
#tempo = 0
#i = 0
#while i < 64:
#    tempo |= (((M >> (tables_des.IP[i] -1)) & 1) << i)
#      i = i + 1
#
##les 16 tours du DES 
#L = (tempo >> 32) 
#R = tempo & MASK32 
#i = 0
#while i < 16 :
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
## echange final entre R et L
## A COMPLETER
#
## Application de la Permutation IP^-1 sur (R16L16)
## le resultat est stocke dans C
#C = 0
#i = 0 
#while i < 64:
#    # A COMPLETER
#print("Crypto = ",hex(C))
#
