def newton_sqrt(nb, max_iter=500, eps=0.00001):
    guess = 1.0
    for i in range(max_iter):
        guess = (guess + nb / guess) / 2
        diff = nb - (guess ** 2)
        if abs(diff) <= eps:
            break
    return guess
