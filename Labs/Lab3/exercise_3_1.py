# Assume that the arguments m and n are integers at least equal to 0.

def f1(m, n):
     L1 = ['_' for _ in range(n)]
     S1 = '|'.join(L1)
     L2 = [S1 for _ in range(m)]
     return ' * '.join(L2)
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE
