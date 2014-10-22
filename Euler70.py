# Find the value of n, 1<n<10^7 for which:
#  - phi(n) is a permutation of n
#  - n/phi(n) is a minimum

# From the second constraint, this would imply
#  that phi(n) should be as large as possible
#  which occurs for the primes, where
#  phi(n) = n-1

# So go through the primes finding their
#  euler's totient and then see if the permutation
#  has the value itself
from __future__ import division
from eulermath import primesieve, eulerphi, array2int, int2array
from itertools import permutations

# Function that quickly checks if y is a permutation of x
# Shoud be faster than listing all permutations and checking those
def checkperm(x,y):
    xa = int2array(x)
    ya = int2array(y)
    isperm = True
    for elem in xa:
        if elem in ya:
            ya.pop(ya.index(elem))
        else:
            isperm = False
            break
    return isperm
    
#for n in primes:
#    pn = n-1
# Euler's totient can be approximated by
#  phi(n) ~= n-1
# So n/phi(n) ~= n/(n-1) ~= 1 for large n
#  We want this to be a minimum, so if phi(n) > n would be okay.
#  But this doesn't happen. So the best we can get is; phi(n) = n
#  Also note phi(p) = p-1 for prime values
#  So we only have to test the primes to 10**7
# Unfortunately, none of the primes are permutations of each other...
# So start with large n...
maxn = 10**7
primes = primesieve(maxn + 1)
nprimes = len(primes)
#cratio = (10,1,1)
ratios = []
for n in primes:
    pn = n - 1
    if checkperm(n,pn):
        print "permutation found %d %d" % (n,pn)
        #if n/pn < cratio[0]:
        #    cratio = (n/pn,n,pn)
            #print "New low value! (ratio,prime,phi(n)) = (%f,%d,%d)" % cratio
        cratio = (n/pn,n,pn)
        print "Appending: (ratio,prime,phi(n)) = (%f,%d,%d)" % cratio
        ratios.append(cratio)
        #print "%f%% complete" % (n/maxn*100)
    #print "%f%% complete" % (n/nprimes*100)

ratios.sort()
minratio = ratios[0]
print "The ratio %f is minimal with n = %d and phi(n) = %d" % minratio
