# Objective is to find the decimal fraction 1/n n<1000 with the longest
#   repeating cycle.
#
# We will use the algorithim outlined in;
#  http://oeis.org/A051626
# Which uses the multiplicative order;
# see http://en.wikipedia.org/wiki/Multiplicative_order
# 10^l = 10^m (mod n)
# then 10^l-10^m mod n = 0 means l-m is the repeating cycle length
# We will also use another sequence;
#  http://oeis.org/A003592
# Which looks for the prime factors of n and returns them minus the set {2,5}
# As it turns out, only 1 is left, then 1/n terminates.

from eulermath import primefactors
from time import sleep

# Returns 1 if the value 1/n is a terminating decimal
#  0 otherwise
def istermdec(n):
    td = 0
    if n == 1:
        td = 1
    else:
        pfac = primefactors(n)
        if 2 in pfac: pfac.remove(2)
        if 5 in pfac: pfac.remove(5)
        if not pfac:
            td = 1
    return td

# Returns the length of the recurring cycle of 1/n
def ncycle(n):
    cyclelen = 0
    if not istermdec(n):
        lpow = 1
        foundcycle = 0
        while not foundcycle:
            for mpow in range(lpow-1,0,-1):
                if (10**lpow - 10**mpow)%n == 0:
                    cyclelen = lpow-mpow
                    foundcycle = 1
                    break
            lpow += 1
    return cyclelen

# Test case, print out the length of the cycles for the first 14 integers
#dmax = 14
#for d in range(1,dmax):
#    print ncycle(d) 

# Now the full 1000 integers
dlimit = 1000
cyclelen = []
for d in range(dlimit):
    cyclelen.append(ncycle(d+1))

cmax = max(cyclelen)
dmax = cyclelen.index(cmax)+1
print "1/%d has the longest cycle at a length of %d" % (dmax,cmax)

