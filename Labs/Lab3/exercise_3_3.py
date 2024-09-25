# Assume that the argument n is an integer at least equal to 0.
#
# Bases range from the smallest possible, at least equal to 2, to 10.
#
# The output is printed out, not returned.

def f3(n):
    n_as_string = str(n)
    min_base = max(2, max({int(d) for d in n_as_string}) + 1)
    for b in range(min_base, 11):
        print(f'{n} is {int(n_as_string, b)} in base {b}')
    pass
    # REPLACE THE PASS STATEMENT ABOVE WITH YOUR CODE
