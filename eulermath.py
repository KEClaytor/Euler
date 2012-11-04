import math
from itertools import izip

#Subfunction that checks to see if a number is prime
# Returns 0 for nonprime, and 1 for prime
def isprime(n):
    prime = 1
    x = 2
    while (x < n/2+1):
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

# Returns the nth triangle number
def tri(n):
    return n*(n+1)/2

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
    iarrs = list(set(iarr))
    if (len(iarr) == len(iarrs)):
        isp = 1
    return isp

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
