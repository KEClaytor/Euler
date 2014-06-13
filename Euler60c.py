# Euler 60 - Find the smallest sum of 5 primes
#            that can be concatenated into
#            other primes

from eulermath import isprimeFermat as isprime
from eulermath import gen_primes
import itertools
from itertools import chain

# What primes can be concatenated to form this prime?
def checkPrime(prime, pairs):
    vs = str(prime)
    cps = []
    for pair in pairs:
        possible = True
        # We have to work for all elements in the pair
        #  in order to form a new tuple
        for elem in pair:
            a = int(str(elem) + vs)
            b = int(vs + str(elem))
            # A prime never begins, nor ends with zero
            #  so we don't have to check that we lost digits
            if not isprime(a) or not isprime(b):
                possible = False
        if possible:
            new = (prime,) + pair
            cps.append(new)
    return cps

if __name__ == "__main__":
    primeListLength = 3
    # First make our prime list
    maxprime = 500000
    primes = gen_primes()
    # Seed us with the pair (3,7) which forms 37 & 73, both prime
    # Search through the higher primes, seeing if they share the
    #   property for all primes in this set
    #   This allows us to form the length 3, 4, and 5 sets.
    pairs = [(3,7)]
    for prime in primes:
        if prime > maxprime:
            break
        if prime < 8:
            continue
        # Get the possible lists we have
        new = checkPrime(prime, pairs)
        if new:
            for item in new:
                print "adding: " + repr(item)
                pairs.append(item)
            # Remove duplicates
            pairs = list(set(pairs))
            # Sort by length
            pairs = sorted(pairs, key=lambda val: len(val))
            print "we now have:"
            print pairs
            if len(pairs[-1]) == 5:
                break

    print "First length-5 tuple found. It's probably the smallest sum:"
    print pairs[-1], sum(pairs[-1])
