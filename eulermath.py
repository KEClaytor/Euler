import math
from itertools import izip

#Subfunction that checks to see if a number is prime
# Returns 0 for nonprime, and 1 for prime
def isprime(n):
    prime = 1
    x = 2
    while (x < n/2):
        if n % x == 0:
            prime = 0 
            break
        x += 1
    return prime 

# Function that transforms a number into a list of digits
#def int2array(n):
#    nlist = []
#    while (n > 0):
#        nlist.append(n % 10)
#        n /= 10 
#    nlist.reverse()
#    return nlist
def int2array(n):
    nlist = [int(i) for i in str(n)]
    return nlist

# Finds the factors of a given number
#  and returns them in a list
#  this form returns 1 and the number
#   itself as a factors
def factors(n):
    factors = []
    if (n == 1):
        factors.append(1)
    for x in range(1,n/2+1):
        if n % x == 0:
            factors.append(x)
            factors.append(n/x)
    factors = list(set(factors))
    factors.sort()
    return factors

# Tests to see if a number is pandigital
def ispandigital(n):
    isp = 0
    iarr = int2array(n)
    iarr.sort()
    iarrs = list(set(iarr))
    if (len(iarr) == len(iarrs)):
        isp = 1
    return isp

# Return nCr
def nCr(n,r):
    if r > n:
        t = n
        n = r
        r = t
    if r > n/2:
        r = n-r
    # izip generates the needed range of pairs (n-r,0), (n-r+1,1), ...
    # The lambda form generates the list of pairs (n-1)C(r-1) nCr
    # And reduce does the multiplication operaton over all elements in the list
    # Grateously stolen from stackexchange
    
    ncr = reduce(lambda x, y: x * y[0] / y[1], izip(xrange(n - r + 1, n+1), xrange(1, r+1)), 1)
    return ncr
