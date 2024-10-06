from math import sqrt


def sieve_of_primes_up_to(n):
    sieve = [True] * (n + 1)
    for p in range(2, round(sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sieve


def tri_numbers(n):
    tris = []
    factors = []
    gaps = []
    sieve = sieve_of_primes_up_to(n)
    for tri in range(1, n + 1):
        if sieve[tri] == False:
            for i1 in range(2, round(sqrt(tri)) + 1):
                if sieve[i1] and tri % i1 == 0:
                    tri1 = tri // i1
                    for i2 in range(i1, round(sqrt(tri1)) + 1):
                        if sieve[i2] and tri1 % i2 == 0:
                            tri2 = tri1 // i2
                            if sieve[tri2] and tri2 != 1:
                                tris.append(tri)
                                factors.append((i1, i2, tri2))
                                gaps.append(min(i2-i1, tri2-i2))
                                break
                    break
    max_gap = max(gaps)
    print(f'There is {len(tris)} trinumber at most equal to {n}.')
    print(f'The largest one is {tris[-1]}, equal to {factors[-1][0]} x {factors[-1][1]} x {factors[-1][2]}.')
    print('')
    print(f'The maximum gap in decompositions is {max_gap}.')
    print('It is achieved with:')
    for i in range(len(gaps)):
        if gaps[i] == max_gap:
            print(f'  {tris[i]} = {factors[i][0]} x {factors[i][1]} x {factors[i][2]}')


tri_numbers(4321)
