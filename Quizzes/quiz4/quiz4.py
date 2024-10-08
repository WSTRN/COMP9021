from math import sqrt


def sieve_of_primes_up_to(n):
    sieve = [True] * (n + 1)
    for p in range(2, round(sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sieve

# def tri_numbers(n):
#     # if n>100000:
#     #     return
#     tris = []
#     factors = []
#     gaps = []
#     sieve = sieve_of_primes_up_to(n)
#     for tri in range(1, n + 1):
#         if sieve[tri] == False:
#             for i1 in range(2, round(sqrt(tri)) + 1):
#                 if sieve[i1] and tri % i1 == 0:
#                     tri1 = tri // i1
#                     for i2 in range(i1, round(sqrt(tri1)) + 1):
#                         if sieve[i2] and tri1 % i2 == 0:
#                             tri2 = tri1 // i2
#                             if sieve[tri2] and tri2 != 1:
#                                 tris.append(tri)
#                                 factors.append((i1, i2, tri2))
#                                 gaps.append(min(i2-i1, tri2-i2))
#                                 break
#                     break
#     max_gap = max(gaps)
#     if len(tris) == 1:
#         print(f'There is {len(tris)} trinumber at most equal to {n}.')
#     else:
#         print(f'There are {len(tris)} trinumbers at most equal to {n}.')
#     print(f'The largest one is {tris[-1]}, equal to {factors[-1][0]} x {factors[-1][1]} x {factors[-1][2]}.')
#     print('')
#     print(f'The maximum gap in decompositions is {max_gap}.')
#     print('It is achieved with:')
#     for i in range(len(gaps)):
#         if gaps[i] == max_gap:
#             print(f'  {tris[i]} = {factors[i][0]} x {factors[i][1]} x {factors[i][2]}')

#fastest
# def tri_numbers(n):
#     if n>100000:
#         return
#     tris = []
#     factors = []
#     gaps = []
#     sieve = sieve_of_primes_up_to(n)
#     for tri in range(1, n + 1):
#         if sieve[tri] == False:
#             for i1 in range(2, round(sqrt(tri)) + 1):
#                 if sieve[i1] and tri % i1 == 0:
#                     tri1 = tri // i1
#                     for i2 in range(i1, round(sqrt(tri1)) + 1):
#                         if sieve[i2] and tri1 % i2 == 0:
#                             tri2 = tri1 // i2
#                             if sieve[tri2] and tri2 != 1:
#                                 tris.append(tri)
#                                 factors.append((i1, i2, tri2))
#                                 gaps.append(min(i2-i1, tri2-i2))
#                                 break
#                     break
#     max_gap = max(gaps)
#     if len(tris) == 1:
#         print(f'There is {len(tris)} trinumber at most equal to {n}.')
#     else:
#         print(f'There are {len(tris)} trinumbers at most equal to {n}.')
#     print(f'The largest one is {tris[-1]}, equal to {factors[-1][0]} x {factors[-1][1]} x {factors[-1][2]}.')
#     print('')
#     print(f'The maximum gap in decompositions is {max_gap}.')
#     print('It is achieved with:')
#     for i in range(len(gaps)):
#         if gaps[i] == max_gap:
#             print(f'  {tris[i]} = {factors[i][0]} x {factors[i][1]} x {factors[i][2]}')


#faster & smaller
def tri_numbers(n):
    cnt_tri = 0
    max_tri = 0
    max_fac = [0, 0, 0]
    max_gap = 0
    tri_max_gap = []
    sieve = sieve_of_primes_up_to(n//4)
    primes = [p for p in range(2, n//4 + 1) if sieve[p]]
    for f1 in range(len(primes)):
        for f2 in range(f1, len(primes)):
            t = primes[f1] * primes[f2]
            if t > n:
                break
            for f3 in range(f2, len(primes)):
                tri = t * primes[f3]
                if tri <= n:
                    cnt_tri += 1
                    if max_tri < tri:
                        max_tri = tri
                        max_fac[0] = primes[f1]
                        max_fac[1] = primes[f2]
                        max_fac[2] = primes[f3]
                    gap = min(primes[f2]-primes[f1], primes[f3]-primes[f2])
                    if gap == max_gap:
                        tri_max_gap.append((tri, primes[f1], primes[f2], primes[f3]))
                    elif gap > max_gap:
                        max_gap = gap
                        tri_max_gap = []
                        tri_max_gap.append((tri, primes[f1], primes[f2], primes[f3]))
                else:
                    break
    tri_max_gap = sorted(tri_max_gap, key=lambda x: x[0])
    if cnt_tri == 1:
        print(f'There is 1 trinumber at most equal to {n}.')
    else:
        print(f'There are {cnt_tri} trinumbers at most equal to {n}.')
    print(f'The largest one is {max_tri}, equal to {max_fac[0]} x {max_fac[1]} x {max_fac[2]}.')
    print('')
    print(f'The maximum gap in decompositions is {max_gap}.')
    print('It is achieved with:')
    for i in range(len(tri_max_gap)):
        print(f'  {tri_max_gap[i][0]} = {tri_max_gap[i][1]} x {tri_max_gap[i][2]} x {tri_max_gap[i][3]}')



# tri_numbers(4321)
tri_numbers(50000000)
