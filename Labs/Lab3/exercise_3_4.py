# Assume that the argument n is an integer at least equal to 0
# and the argument base is an integer between 2 and 9 included.

def f4(n, base):
    D = {0: (0,)}
    for m in range(1, n + 1):
        digits = []
        p = m
        while p:
            digits.append(p % base)
            p //= base
        D[m] = tuple(reversed(digits))
    return D
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE
