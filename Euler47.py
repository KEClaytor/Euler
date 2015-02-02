# Find the first four consecutive numbers to have four distinct prime factors

from eulermath import nthprime, isprime, primefactors


# I would like to move this to eulermath, but it does
# not give the right results there!
# Return the prime factors of a number
def primefactors(n):
    pf = []
    while not isprime(n):
        founddiv = False
        pi = 1
        while not founddiv:
            pn = nthprime(pi)
            # This prime evenly divides, factor it out
            if n % pn == 0:
                n = n/pn
                pf.append(pn)
                founddiv = True
            pi += 1

    # Note: we have also reduced n down to a prime, include it as well
    pf.append(n)
    return pf


def collapse_prime_factors(pf):
    spf = set(pf)
    c = []
    for x in spf:
        c.append(x**pf.count(x))
    return c


def nuniquefac(faclist):
    return list(set([x for p in faclist for x in p]))

if __name__ == "__main__":
    # Length of prime factor check
    # lpfc = 2 should find 14 and 15 as the first two
    # lpfc = 3 should find 644, 645, 646 as the first three
    lpfc = 4
    pf = [0]*lpfc
    nl = [0]*lpfc
    cnum = 2
    for ii in range(lpfc):
        nl[ii] = cnum
        pf[ii] = collapse_prime_factors(primefactors(cnum))
        cnum += 1

    while len(nuniquefac(pf)) != lpfc**2:
        nl.pop(0)
        nl.append(cnum)
        pf.pop(0)
        pf.append(collapse_prime_factors(primefactors(cnum)))
        cnum += 1

    for ii in range(lpfc):
        print "%d = %s" % (nl[ii], repr(pf[ii]))

    # testval = 12
    # print primefactors(testval)
    # print collapse_prime_factors(primefactors(testval))
