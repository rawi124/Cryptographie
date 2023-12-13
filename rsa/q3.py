def is_on(Q,a,b,p):
    return (Q[1] ** 2) % p == ((Q[0] ** 3 + a * Q[0] + b) % p)

print(is_on((193, 70),332,474,479))

