def double(P,p):
    x_P, y_P = P[0], P[1]
    s = inverse(((3 * (x_P**2)) -3) , (2*y_P ))
    xr = ((s**2) - (2 * x_P)) % p
    yr = (s * (x_P - xr ) - y_P) % p
    return [xr, yr]
