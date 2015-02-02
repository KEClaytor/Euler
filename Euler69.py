# Find the largest value of n/\phi(n) for n <= 1M

from __future__ import division
from eulermath import eulerphi

if __name__ == "__main__":
    nmax = 0
    rmax = 1
    print "n phi(n) n/phi(n)"
    for n in range(1, 10**6+1):
        pn = eulerphi(n)
        if n/pn > rmax:
            nmax = n
            rmax = n/pn
            print "New max: " + repr(n)

    print "The maximum ratio occurs for n = %d" % (nmax)
