import random
import time

PIN = ['2', '3', '9', '7', '5', '3', '8', '1',
       '0', '5', '4', '6', '9', '7', '5', '4']


def verifie(code, pin):
    """
    retourne True si le code en parametre est egale 
    au pin du cours
    """
    i = 0
    while i < 16:
        #time.sleep(0.2)
        if code[i] != pin[i]:
            return False
        i += 1
    return True


def pin16(code):
    """
    effectue une attaque pour retrouver le meme code en entree
    la complexite de ce code est de O(10^16) si on considere 
    un code pin a 16 chiffres
    """
    for _ in range(10**16): 
        cod_str = ''.join(str(random.randint(0, 9)) for _ in range(16))
        if verifie(cod_str, code):
            return cod_str
    return None

def permutation_alea():
    """
    effectue une permutation alea en utilisant l algo de Fisher-Yates
    """
    permutation = []
    for i in range(16):
        permutation.append(i)
    i = 15
    while i > 0 :
        j = random(i+1)
        permutation[i], permutation[j] = permutation[j], permutation[i]
        i -= 1


if __name__ == "__main__":
    print("teste de la fonction pin16", pin16(PIN))
    print("verification du meme code pin ", verifie(PIN,PIN))

