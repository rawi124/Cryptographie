def add(P,Q,p):
    yp, xp = P[1], P[0]
    yq, xq = Q[1], Q[0]
    s = yp-yq * inverse((xp-yp), p)
    xr = s**2 -xp - xq
    yr = s*(xp-xr) - yp
    return xr, y 
~                          
