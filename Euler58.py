# Form a spiral of numbers, interestingly there are quite a few primes on the diagonal.
# for what side length does the ratio of primes fall to <10%?

from __future__ import division
from eulermath import primesieve

# Get all the diagonal values for a given (odd) side length
def getdiags(side):
    offset = (side-2)**2 + (side-1)
    diag = range(offset,side**2+1,side-1)
    return diag

if __name__ == "__main__":
    ntotalprime = 0  # Starting on side length 1 we have zero primes
    ndiag = 1        # with only 1
    pside = 26507
    side = 3
    fracprime = 1.00
    # Only increment this if we have to
    print "Pre-computing prime list, please hold on..."
    primes = set(primesieve(pside**2+1))
    while side < 50 or fracprime > 0.1:
        diag = getdiags(side)
        nprime = len(primes.intersection(diag))
        ntotalprime += nprime
        ndiag += 4
        fracprime = ntotalprime/ndiag
        print side, fracprime
        side += 2

    print "Side length for which the ratio of primes is < 10% is: " + repr(side-2)
