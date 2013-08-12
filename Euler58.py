# Form a spiral of numbers, interestingly there are quite a few primes on the diagonal.
# for what side length does the ratio of primes fall to <10%?

from __future__ import division
from eulermath import isprime

smax = 11
side = 3
nprime = 0
nnotprime = 0
fracprime = 1
while (fracprime > .1):
    offset = (side-2)**2 + (side-1)
    diag = range(offset,side**2+1,side-1)
    for elem in diag:
        if isprime(elem):
            nprime += 1
        else:
            nnotprime += 1
    fracprime = nprime/nnotprime
    print side, fracprime
    side += 2

print "Side length for which the ratio of primes is < 10% is: " + repr(side-2)
