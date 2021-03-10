def newton_sqrt(n, max_iter=500):
    g = n
    for i in range(max_iter):
        g = 0.5 * (n + g / n)
        if g ** 2 == n:
            break
    return g
