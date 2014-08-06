import math
import array
from itertools import izip
from itertools import permutations, combinations
from fractions import Fraction
import random
import numpy

#Subfunction that checks to see if a number is prime
# Returns 0 for nonprime, and 1 for prime
def isprime(n):
	if n > 1:
		prime = 1
		x = 2
		while (x < n/2+1):
			if (n % x == 0):
				prime = 0 
				break
			x += 1
	else:
		prime = 0
	return prime 

# Find prime numbers in a list
def find_primes_in_list(testlist):
    prime_list = []
    for val in testlist:
        if isprime(val):
            prime_list.append(val)
    return prime_list

# Another isprime function that searches our primelist
def isprimelist(n):
	pfile = open("eplist.dat")
	plist = [int(x) for x in pfile]
	prime = plist.count(n)
	return prime

# A faster check for prime numbers
def isprimeFermat(number):
    # if number != 1
    if (number > 1):
        # repeat the test few times
        for time in range(3):
            # Draw a RANDOM number in range of number ( Z_number )
            randomNumber = random.randint(2, number)-1

            # Test if a^(n-1) = 1 mod n
            if ( pow(randomNumber, number-1, number) != 1 ):
                return False

        return True
    else:
        # case number == 1
        return False  

# Quickly return the nth prime from our list
def nthprime(n):
    pfile = open("eplist.dat")
    for x in range(n-1):
        pfile.readline()
    return int(pfile.readline())

# Stac numpy based prime sieve
def primesieve(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
    for i in xrange(1,int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}  

    # The running integer that's checked for primeness
    q = 2  

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q        
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

# Function that transforms a number into a list of digits
def int2array(n):
    nlist = [int(i) for i in str(n)]
    return nlist

# And the reverse
def array2int(arr):
    rint = 0
    if (len(arr) > 0):
        arrstr = ''
        for x in arr:
            arrstr = ''.join([arrstr,str(x)])
    rint = int(arrstr)
    return rint

# returns the difference of consecutive elements in an array
def arraydiff(arr):
    d = []
    for ii in range(len(arr)-1):
        d.append(arr[ii+1] - arr[ii])
    return d

# Returns the nth triangle number
def tri(n):
    return n*(n+1)/2
# Returns the nth pentagonal number
def pent(n):
    return n*(3*n-1)/2
# Returns the nth hexagonal number
def hex(n):
    return n*(2*n-1)

# Tests to see if a number is triangular
#  (pentagonal, hexagonal), and returns
#  the index of that number, or zero if it is not
# Eg; x = tri(n) -> returns n
# We can ignore the negative root as we are not
#  intrested in n<0
def istri(x):
    ist = 0
    n = (-1 + math.sqrt(1+8*x) )/2
    if not isinstance(n, complex):
        if n == round(n):
            ist = n
    return ist
def ispent(x):
    isp = 0
    n = (1 + math.sqrt(1+24*x) )/6
    if not isinstance(n, complex):
        if n == round(n):
            isp = n
    return isp
def ishex(x):
    ish = 0
    n = (1 + math.sqrt(1+8*x) )/4
    if not isinstance(n, complex):
        if n == round(n):
            ish = n
    return ish

# Integer element cyclic permutation
def intcpermute(n):
    sper = []
    iword = str(n)
    for x in range(1,len(iword)+1):
        sper.append(iword)
        iword = iword[1:] + iword[0]
    return map(int, sper)

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

def primefactors(n):
    allfac = factors(n)
    primefac = []
    for fac in allfac:
        if isprime(fac):
            primefac.append(fac)
    return primefac

# Determine the greatest common factor / denominator of two values
def gcd(a, b):
    fa = factors(a)
    fb = factors(b)
    cf = set(fa).intersection(set(fb))
    gcd = max(cf)
    return gcd

# A faster prime factorization using the prime sieve
def primefac(n):
    if n < 6:
        primes = primesieve(6)
    else:
        primes = primesieve(n+1)
    pf = []
    while n not in primes:
        for x in primes:
            if n%x == 0:
                pf.append(x)
                n = n/x
                break
    pf.append(n)
    return hist(pf)

# The euler phi / totient function
def eulerphi(val):
    ep = val
    if val > 1:
        [p,n] = primefac(val)
        for ii in range(len(p)):
            ep *= ( 1 - 1/(1.0*p[ii]) )
    return int(ep)

def wordworth(word):
    worth = 0
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for letter in word:
        # Add the index to the name value, account for the zero offset
        worth += alphabet.index(letter) + 1
    return worth

# takes in a roman numeral (string)
#  and converts it to an integer
#  In the case of failure, returns 0
#  This error checking is not fully implemented yet
def roman2int(rstr):
    rchar = ["M","D","C","L","X","V","I"]
    rval = [1000,500,100,50,10,5,1]
    val = 0
    ii = 0
    while ii < len(rstr)-1:
        cval = rval[rchar.index(rstr[ii])]
        nval = rval[rchar.index(rstr[ii+1])]
        if nval > cval:
            val += nval-cval
            ii += 2
        else:
            val += cval
            ii += 1
    # If we skipped two, we still need to do the last
    if ii < len(rstr):
        cval = rval[rchar.index(rstr[ii])]
        val += cval
    return val

def int2roman(n):
    # The only tricky thing here is we build the string in reverse order
    r1s = "IXCM"
    r5s = "VLD"
    ind = 0
    rstr = ""
    if n < 4999:
        while n > 0:
            if n%10 >= 5:
                if n%5==0:
                    rstr += (r5s[ind])
                elif n%5==4:
                    rstr += (r1s[ind+1])
                    rstr += (r1s[ind])
                else:
                    rstr += (r1s[ind]*(n%5))
                    rstr += (r5s[ind])
            else:
                if (n%5==4)&(ind!=3):
                    rstr += (r5s[ind])
                    rstr += (r1s[ind])
                else:
                    rstr += (r1s[ind]*(n%5))
            n = (n - n%5) / 10
            ind += 1
    return rstr[::-1]

# Tests to see if a number is pandigital
def ispandigital(n):
    isp = 0
    iarr = int2array(n)
    iarr.sort()
    rint = range(1,len(iarr)+1)
    if (iarr == rint):
        isp = 1
    return isp

# Makes all pandigital numbers of length n
# Returns an iterator
def makepandigital(n, reverse=False, low=1):
    rint = range(low,n+1)
    if reverse:
        rint.reverse()
    npermute = n+1-low
    perms = permutations(rint,npermute)
    return perms

# Checks to see if a number is a palindrome
def intreverse(n):
    intstring = str(n)
    return int(intstring[::-1])
 
def ispalindrome(n):
    isp = 1
    pal = str(n)
    lap = pal[::-1]
    for ii in range(0,len(pal)):
        if (pal[ii] != lap[ii]):
            isp = 0
            break
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


# The coin change problem can be solved by the help of generating functions
#  from combinatorics
# The ways of making change for p cents is the coefficient of x^p in
#  expanding; 1/((1 - x)(1 - x^5)(1 - x^10)...(1 - x^largestchange))
# For the reasoning, let's take the simple example of making change using
#  only 5c pieces, we have 1 way of making zero cents, 1 way of making 5c, ...
# Hence; 1 + x^5 + x^10 + x^15 = 1/(1 - x^5)
# We multiply by the generating functions for other coin denominations
#  to obtain the above sequence. I'll implement this method for finding that
#  coefficient;
# http://math.stackexchange.com/questions/176363/keep-getting-generating-function-wrong/176397#176397
def coinage(amt,coins):
    rval = 0
    # Make sure that we have a set of coins
    if len(coins) > 0:
        if (amt < coins[-1]):
            # we have to populate at least up to the max coin value
            val = amt
            amt = coins[-1]
        else:
            val = amt
        c = array.array('i',(0,)*(amt+1))
        c[0] = 1
        for k in coins:
            for i in range(amt-k+1):
                c[i+k] += c[i]
        rval = c[val]     
    return rval

# Determine if this list is an arithemetric series
def is_arith_series(test):
    tl = list(test)
    tl.sort()
    isas = False
    if len(list(set(arraydiff(tl)))) == 1:
        isas = True
    return isas
    
# We want to find an arithemetric series of some length in this sequence
def find_arithemetric_series(testlist, a_len = 0):
    series = []
    if a_len == 0:
        # Get the sub-lists of various length
        for m in range(2,len(testlist)+1):
            combs = [ii for ii in combinations(testlist,m)]
            for tl in combs:
                if is_arith_series(tl):
                    series.append(tl)
    else:
        # Otherwise just get the arithemetric series of a particular length
        combs = [ii for ii in combinations(testlist,a_len)]
        for tl in combs:
            if is_arith_series(tl):
                series.append(tl)
    return series
 
###
### Functions for working with continued fractions
###

# Helper function to make a string of a fraction
def frac2str(frac):
    return "%d/%d"%(frac.numerator,frac.denominator)

def makecontfrac(arr):
    if len(arr) > 1:
        rfrac = Fraction(arr[0],1) + 1/makecontfrac(arr[1::])
    else:
        rfrac = Fraction(1,arr[0])
    return rfrac

# Histogram-ing function: takes in a list and returns
#  the sorted unique values of that list
#  and their corresponding counts
def hist(listin):
    outvals = list(set(listin))
    outvals.sort()
    outcnts = [listin.count(x) for x in outvals]
    return (outvals, outcnts)

