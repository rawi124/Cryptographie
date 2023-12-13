from random import *
def point_of(a,b,p):
    x = randint(0, p-1) % p
    y2 = (x ** 3 + a* x + b) % p
    while pow(y2, (p-1) //2, p) != 1 :
        x = randint(0, p-1) % p
        y2 = (x ** 3 + a* x + b) % p
    y = pow(y2, (p-1)//4, p)
    return x, y


