import random
import time
import subprocess


PIN = ['2', '3', '9', '7', '5', '3', '8', '1',
       '0', '5', '4', '6', '9', '7', '5', '4']


def verifie(code, pin):
    """
    retourne True si le code en parametre est egale 
    au pin du cours
    """
    i = 0
    while i < 16:
        # time.sleep(0.2)
        if code[i] != pin[i]:
            return False
        i += 1
    return True


def pin_attaque_c(executable, longeur):
    """
    effectue une attaque pour retrouver le code pin4
    en executant le code pin4.c qui une fois 
    on est sur un bon chiffre a la position i, le temps
    d execution est allonge
    """
    i = 0
    cle_probable = ""
    while i < longeur:
        temps = -1
        for k in range(10):
            tmp = cle_probable + str(k) + "0" * \
                (longeur - len(cle_probable) - 1)
            debut = time.time()
            subprocess.run(
                [executable, tmp], capture_output=True, text=True)
            fin = time.time()
            temps_exec = fin - debut
            if temps < temps_exec:
                k_prob = str(k)
                temps = temps_exec
        cle_probable += k_prob
        i += 1
    return cle_probable


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


if __name__ == "__main__":
    # print("teste de la fonction pin16", pin16(PIN))
    # print("verification du meme code pin ", verifie(PIN,PIN))
    # print(pin_attaque_c("./pin4", 4))
    print(pin_attaque_c("./pin16a", 16))
