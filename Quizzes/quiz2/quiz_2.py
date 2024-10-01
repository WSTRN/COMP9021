# Written by *** for COMP9021
#
# Defines a function apply_pattern_to_list(), that takes three arguments.
# You can assume that the first argument is a list L of integers,
# the second argument is a nonempty string (the pattern) consisting of
# + and - only (it is set to '+-' by default),
# and the third argument is either True or False
# (it is set to True by default).
#
# * If the third argument is True then is removed, again and again,
#   the leftmost element in L that prevents what is left of L,
#   from the beginning up to that element, to be consistent with
#   the pattern, read from left to right.
#   .
# * If the third argument is False then is removed, again and again,
#   the rightmost element in L that prevents what is left of L,
#   from that element up to the end, to be consistent with the pattern,
#   read from right to left.
#
# * A + in the pattern is for two successive elements the second of which
# is strictly greater than the first one.
# * A - in the pattern is for two successive elements the second of which
# is strictly smaller than the first one.
#
# The pattern is to be thought of as circular (as if wrapping around),
# so there is no difference between a pattern and many concatenations
# of that pattern (e.g., there is no difference between the patterns
# '+', '++', '+++', ..., and there is no difference between the patterns
# '+-', '+-+-', '+-+-+-'...
#
# The function returns a dictionary for everything that has been
# removed from L: where in the created list an element has been
# removed (the key, as a positive index when processing list and pattern
# from left to right, as a negative index when processing list and pattern
# from right to left), and what that element is (the value).


# The function modifies the list provided as argument
# and returns a dictionary.
from itertools import cycle

def apply_pattern_to_list(L, pattern='+-', from_start=True):
    #print(L)
    #print(pattern)
    state = True
    cnt = 0
    out = {}
    if from_start:
        # print(from_start)
        while state:
            cycle_pattern = cycle(pattern)
            state = False
            for i in range(len(L)-1):
                p = next(cycle_pattern)
                # print(i, L[i], L[i+1], p)
                if (p == '+' and L[i] >= L[i+1]) or (p == '-' and L[i] <= L[i+1]):
                    # print('------------\n', i, L[i], L[i+1], p)
                    out[i+1+cnt] = L[i+1]
                    cnt += 1
                    L.pop(i+1)
                    state = True
                    break
            # print(L)
    else:
        #print(from_start)
        pattern = pattern[::-1]
        while state:
            cycle_pattern = cycle(pattern)
            state = False
            for i in range(-2, -1 - len(L), -1):
                p = next(cycle_pattern)
                #print(i, L[i], L[i+1], p)
                if (p == '+' and L[i+1]>= L[i]) or (p == '-' and L[i+1] <= L[i]):
                    #print('------------\n', i, L[i], L[i+1], p)
                    out[i-cnt] = L[i]
                    cnt += 1
                    L.pop(i)
                    state = True
                    break
            #print(L)
    #print(out)
    return out
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE
