def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res
    

def jaccard_dist(x, y):
    up = 0
    down = len(x)
    for i in range(len(x)):
        if(x[i] == y[i]):
            up += 1
    if (down == 0):
        down = 1
    res = 1 - up/down
    return res

def cosine_sim(x, y):
    a = 0
    b = 0
    c = 0
    for i in range(len(x)):
        a += x[i] * y[i]
        b += x[i]**2
        c += y[i]**2
    
    numer = ((b**(1/2))*(c**(1/2)))
    if(numer == 0):
        numer = 1

    res = a / numer

    return res

# Feel free to add more
