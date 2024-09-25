# Written by *** for COMP9021
#
# Two functions to implement.
#
#
# The function picture() takes two integers as arguments,
# that you can assume are both at least equal to 1;
# it prints out a "picture", that note has no trailing
# spaces on any line.
#
# You might find the rstrip() string method useful. 
#
#
# The function list_of_tuples() takes a string as argument,
# that you can assume is the name of a file that exists
# in the working directory.
#
# The file can contain anywhere any number of blank lines
# (that is, lines containing an arbitrary number of spaces
# and tabs--an empty line being the limiting case).
#
# Nonblank lines are always of the form:
#                a:b!c
# with any number of spaces at the beginning and at the end of the line
# (possibly none) and any number of spaces around : and around !
# (possibly none).
# When a < b < c, a tuple is added to the list that is eventually
# returned.
import re

def picture(m, n):
    cnt = n - 1

    s1 = ' /'
    s2 = '/ '
    s3 = '\\ '
    s4 = ' \\'

    while cnt:
        cnt = cnt - 1
        s1 += '\\/'
        s2 += '__'
        s3 += '  '
        s4 += '/\\'

    s1 += '\\ '
    s2 += ' \\'
    s3 += ' /'
    s4 += '/ '

    cnt = m
    o1 = ''
    o2 = ''
    o3 = ''
    o4 = ''
    while cnt:
        cnt = cnt - 1
        o1 = o1 + s1
        o2 = o2 + s2
        o3 = o3 + s3
        o4 = o4 + s4
    print(o1.rstrip(' '))
    print(o2)
    print(o3)
    print(o4.rstrip(' '))
    pass
    # REPLACE PASS ABOVE WITH YOUR CODE

def list_of_tuples(filename):
    with open(filename) as f:
        s = f.read()
        f.close()
    out = []
    s = s.replace('\t', '')
    s = s.replace(' ', '')
    lines = s.splitlines()
    lines = list(filter(None, lines))
    # print(lines)
    for line in lines:
        e = re.split('[:!]', line)
        # e = list(filter(None, e))
        # print(e)
        res = [eval(i) for i in e]
        if res[0]<res[1] and res[1]<res[2]:
            t = (res[0], res[1], res[2])
            out.append(t)
            # print(t)
    # print(out)
    return out
    # REPLACE THE RETURN ABOVE WITH YOUR CODE










