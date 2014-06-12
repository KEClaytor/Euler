# Euler 60
# Find the list of five primes whereby one can take any two
#  and concatenate them in any order and obtain a prime.

from eulermath import primesieve

if __name__=="__main__":
    nmax = 100000000
    primes = primesieve(nmax)
    print primes
    # Hint: we'll be expanding this list
    sequence = [3, 7]
    for prime in primes:
        works = True
        for cp in sequence:
            cata = int(str(prime) + str(cp))
            catb = int(str(cp) + str(prime))
            if (cata < nmax) and (catb < nmax):
                if (cata not in primes) or (catb not in primes):
                    works = False
            else:
                works = False
        if works:
            sequence.append(prime)
            print sequence
    print sequence
