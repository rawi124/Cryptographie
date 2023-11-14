def multbyalpha(b,f):
    """
    multiplie b par alpha
    """
    n = len(bin(f)) - 3
    y = b << 1 # ajoute un zero a droite donc effectue la multiplication
    # si le bit du poids le plus fort est a 1
    # alors le produit a depasse le degre du polynome f
    # et donc on fait un xor pour rester dans le corps
    if y & ( 1 << n) :
        y ^= f
    return y

def multiplication(b,c,f):
    """
    effectue la multiplication de b * c
    
    """
    S = 0
    x = b
    while c != 0:
        bit = c & 1
        if bit != 0:
            S = S ^ x
        x = multbyalpha(x,f)
        c = c >> 1
    return S

def table_alpha(P):
    """
    genere une table d elements dans un corps fini
    base sur un polynome irreductible
    """
    # -3 : -2 pour 0b et -1 pour l entier dans le polynome ( degre 0 )
    degree_poly = len(bin(P))-3
    nbr_elements = (1<<degree_poly) -1 # 2 ** degre - 1
    L     = [0]*nbr_elements
    L[0]  = 1
    alpha = 1
    i     = 1
    while i < nbr_elements:
        alpha = multbyalpha(alpha,P)
        L[i] = alpha
        i+=1
    return L

def is_irreductible(P,p):
    """
    retourne si P es irreductible ou pas
    """
    i = 0
    eval = 1
    while (i+1) < p and eval:
        eval = (P[0]*i + P[1])%p
        j = 2
        while j < len(P) :
            eval = (eval*i + P[j])%p
            j += 1
        i += 1
    return bool(eval)

def is_primitif(P):
    """
    """
    degree_poly = len(P) - 1
    nbr_elements = (1 << degree_poly) - 1
    div = decompose(nbr_elements)
    i = 0
    while i < len(div):
        exp = nbr_elements/div[i]
        res = 1
        j = 0
        while j < exp:
            res = multiplie(res, 2, P)
            j += 1
        if res == 1:
            return False
        i += 1
    return True

def eval_poly(P, b): #ne marche que pour poly de degree 2 ou superieur
    eval = P[0]
    i = 1
    while i < len(P) :
        eval = eval*b + P[i]*
        i += 1
  return eval

def decomposePremiers(n):
    listePremier = []
    if n%2 == 0:
        listePremier += [2]
    while n%2 == 0:
        n = n//2
    i = 3
    while n != 1 :
        if n%i == 0 :
            listePremier += [i]
        while n % i == 0 :
            n = n // i
        i += 2
    return listePremier
