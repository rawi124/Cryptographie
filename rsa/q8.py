def calcul_point(k,P,p):
    """
    effectue double and add
    """
    n = k
    cpt = 0
    while n :
        n >>= 1
        cpt += 1
    Q = P
    tmp = 1 << (cpt-2)
    while tmp :
        Q = double(Q, P)
        if k & tmp :
            Q = add(Q, P, p
        tmp >>= 1
    return Q 
