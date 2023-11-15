def decompose(n, b):
    """
    decompose l entier n dans la base b
    """
    res = []
    while n > 0 :
        res.append(n%b)
        n = n // b
    return res[::-1]

def entier(liste, b):
    """
    retoune l entier decomposee en base b
    """
    s = 0
    i = 0
    while i < len(liste) :
        s += liste[i] * b**i
        i += 1
    return s

def pgcd(a,b):
    while b != 0 :
        a, b = b, a%b
    return a

def exp(a,x,n):
    """
    effectue le pow
    """
    res = 1
    a = a%n
    while x != 0 :
        if x % 2 :
            res = (res * a) % n
        a = (a * a) % n
        x = x // 2
    return res

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


# Générer une liste de n entiers congrus à c modulo mod
def list_congru(n,c,mod):
    #L = [i for i in range(1, 100) if i % 7 == 21 % 7 and i != 21][:5]
    #L = [c+mod * k for k in range(1,n+1)]
    return [c + mod * k for k in range(n)]

def produit_scalaire_mod(u, v, mod):
    return sum((a * b) % mod for a, b in zip(u, v)) % mod


def find_generators(modulo): #+ 
    generators = [i for i in range(1, modulo) if math.gcd(i, modulo) == 1]
    return generators

def generateurs_x(n): #*
  gen_list = []
  prime_num = decomposePremiers(n-1)
  i = 1 
  while i < n:
    j=0
    boolean = True
    while j < len(prime_num) and boolean:
      if pow(i,(n-1)//prime_num[j],n) == 1:
        boolean = False
      j += 1
    if boolean == True:
      gen_list += [i]
    i += 1
  return gen_list

def find_generators(modulo): #*
    #from sympy import totient
    return totient(modulo - 1)


def ordre_element(element, modulo): #+
    for j in range(1, modulo):
        if j != 0:
            if (element * j) % modulo == 0:
                return j
    return None 

def ordre(a, n):
    true_n = n 
    while a != 0 :
        n, a = a, n%a
    return true_n//n 

def ordre_element(element, modulo): #*
    result = element
    order = 1
    while result != 1:
        result = (result * element) % modulo
        order += 1
    return order

def ordre(a,p): #*
  i = 1
  omin = p
  while i <= (p-1)**0.5 :
    if (p-1) % i == 0:
      if pow(a,i,p) == 1:
        return i 
      if pow(a,(p-1)//i,p) == 1:
        if omin > (p-1)/i:
          omin = (p-1)/i 
    i += 1
  return omin 

def inverse_modulo_list(modulo): #liste des éléments (et de leur inverse) de  Z/moduloZ
    inverses = {}
    for a in range(1, modulo):
        for i in range(1, modulo):
            if (a * i) % modulo == 1:
                inverses[a] = i
                break 
    return inverses

def phi_function(n): #euler 
    count = 0
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            count += 1
    return count

def euclidean_extended_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = euclidean_extended_algorithm(b, a % b)
        return d, y, x - y * (a // b)

def inverse_modulo(a, m): #inverse de a mod m
    d, x, y = euclidean_extended_algorithm(a, m)
    if d == 1:
        return x % m
    else:
        return None
    
def exp(a,x,n): #renvoie a^x modulo n
    res = 1
    base = a #a&n
    while x != 0:
        if x % 2 :
            res = (res * base) % n
        base = (base * base) % n
        x //= 2
    return res

def matmat_f(A,B,P):
    C = []
    for i in range(len(A)):
        L = []
        for j in range(len(B[0])):
            res = 0
            for k in range(len(B)):
                res ^= multiplie(A[i][k],B[k][j],P)
            L.append(res)
        C.append(L)
    return C
