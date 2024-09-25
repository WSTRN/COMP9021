# Assume that the argument integral_part is an integer at least equal to 0
# and the argument fractional_part is an integer strictly greater than 0.
#
# The output is printed out, not returned.

def f5(integral_part, fractional_part):
    precision = len(str(fractional_part))
    a_float = float(str(integral_part) + '.' + str(fractional_part))
    simple_precision = f'{a_float:.{precision}f}'
    extended_simple_precision = simple_precision + '0' * precision
    double_precision = f'{a_float:.{precision * 2}f}'
    print('With', precision * 2, 'digits after the decimal point, ', end='')
    if extended_simple_precision == double_precision:
        if precision == 1:
            trailing_zeros_text = 'zero,'
        else:
            trailing_zeros_text = 'zeroes,'
        print(simple_precision, 'prints out with', precision, 'trailing', trailing_zeros_text, 'namely, as', extended_simple_precision)
    else:
        print(simple_precision, 'prints out as', double_precision)
    # REPLACE THE PASS STATEMENT ABOVE WITH YOUR CODE
