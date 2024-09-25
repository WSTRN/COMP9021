# Assume that the argument n is an integer at least equal to 0.
#
# Even digits are white, odd digits are black.
#
# The output is printed out, not returned.

def f2(n):
    d = {0: '\u2b1c', 1: '\u2b1b'}
    L = [d[int(c) % 2] for c in str(n)]
    print(''.join(L))
    return ''
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE
