# Form a spiral of numbers, interestingly there are quite a few primes on the diagonal.
# for what side length does the ratio of primes fall to <10%?

from __future__ import division
from eulermath import primesieve

# Get all the diagonal values for a given (odd) side length
def getdiags(side):
    diag = [1]
    for tside in range(3,side+1,2):
        offset = (tside-2)**2 + (tside-1)
        for x in range(offset,tside**2+1,tside-1):
            diag.append(x)
    return diag

side = 26507
sideinc = 200
fracprime = 1
found = False
# Only increment this if we have to
primes = primesieve(side**2+1)
while (sideinc > 2):
    # make sure side is an odd length
    if side%2 == 0:
        side = side+1
    diag = getdiags(side)
    nprime = len(list(set(primes).intersection(diag)))
    ndiag = len(diag)
    fracprime = nprime/ndiag
    print side, fracprime
    if fracprime >= .1:
        side += sideinc
        primes = primesieve(side**2+1)
    else:
        sideinc = sideinc//2
        side -= sideinc

print "Side length for which the ratio of primes is < 10% is: " + repr(side)
