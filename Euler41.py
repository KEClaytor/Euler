# Find the largest n-digit pandigital prime

from eulermath import makepandigital, isprime, array2int

# We cap off at 987654321
# Search primes up to that point and decide if they are pandigital

# Start large and go small
# That way the first one we find will be the largest
def findlargestpandigital():
    for n in range(9,1,-1):
        pan = makepandigital(n,True)
        for p in pan:
            pint = array2int(p)
            #print "Testing: " + repr(pint)
            if isprime(pint):
                print "Found the largest pandigital prime: " + repr(pint)
                return pint

findlargestpandigital()
