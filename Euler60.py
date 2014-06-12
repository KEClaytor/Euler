# Euler 60 - Find the smallest sum of 5 primes
#            that can be concatenated into
#            other primes

from eulermath import primesieve
import itertools
from itertools import chain

# What primes can be concatenated to form this prime?
def concatenatedPrimes(val, primes):
    vs = str(val)
    cps = []
    for ii in range(len(vs)-1):
        va = int(vs[:ii+1])
        vb = int(vs[ii+1:])
        # Make sure we didn't truncate a zero
        if len(str(va) + str(vb)) == len(vs):
            if (va in primes) and (vb in primes):
                #print "Testing val: %d\tsplit into: %d and %d are both prime" % (val, va, vb)
                cps.append((va, vb))
    return cps

# Flattens, removes duplicates, and sorts values from lists of tuples
def flattenTupleList(tlist):
    return sorted(list(set([x for x in chain.from_iterable(tlist)])))

if __name__ == "__main__":
    primeListLength = 3
    # First make our prime list
    primes = primesieve(100000)
    # Then sort through them seeing if we can
    #  split them into smaller primes. If so, store the splits
    pairs = []
    for prime in primes:
        if prime > 10:
            possible = concatenatedPrimes(prime, primes)
            if possible:
                for x in possible:
                    pairs.append(x)

    # Remove exact duplicates
    pairs = sorted(list(set(pairs)), key=lambda val: sum(val))
    # Remove any pairs that do not have their reverse in the list
    newpairs = pairs[0::]
    for pair in pairs:
        rev = pair[::-1]
        #print "Testing " + repr(pair) + " with reflection: " + repr(rev)
        if rev not in pairs:
            #print repr(pair) + " has no reflection, removing: " + repr(pair)
            newpairs.remove(pair)
    # Sort by sum of pairs
    newpairs = sorted(newpairs, key=lambda val: sum(val))
    allvalues = flattenTupleList(newpairs)
    # Find which other values these can pair with
    allpartners = []
    for x in allvalues:
        xpartners = flattenTupleList([item for item in newpairs if x in item])
        allpartners.append(sorted(xpartners))
        #print x, xpartners

    # A given value will for a tuple based on which of it's subsets are complete
    possible = []
    for ii in range(len(allvalues)):
        subsets = []
        for x in allpartners[ii]:
            subsets.append(allpartners[allvalues.index(x)])
        # Find the intersection of these sub-lists
        isect = list(set(subsets[0]).intersection(*subsets))
        possible.append(isect)

    possible = [x for x in possible if len(x) > 1]
    possible = sorted(possible, key=lambda val: sum(val))
    print "Found some combinations that work (sorted by sum of list):"
    print possible

    properLength = [x for x in possible if len(x) >= primeListLength]
    print "Here are those whose length >= %d (sorted by sum of list):" % (primeListLength)
    print properLength
