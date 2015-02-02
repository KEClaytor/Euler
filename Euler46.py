# Find the smallest odd composite that cannot be written as
#  the sum of a prime and twice a square:
# OC =?= P + 2x(i)^2
from eulermath import isprime


# make an odd composite from 1 <= j <= i
def moc(i, j):
    if j > i:
        j = i
        print "invalid value of j, trimming to i"
    return (2*i+1)*(2*j+1)


# Tests to see if this number can be written as
#  the sum of a prime and twice a square
def isPp2Sq(num):
    i = 1
    rval = 0
    while 2*(i**2) < num:
        res = num - 2*(i**2)
        if isprime(res):
            # We can do the decomposition
            rval = 1
            break
        i += 1
    return rval

if __name__ == "__main__":
    found = False
    i = 1
    j = 1
    while not found:
        # Test to see if we need to increment i
        if j > i:
            i += 1
            j = 1
        # If this odd composite cannot be decomposed
        oc = moc(i, j)
        if not isPp2Sq(oc):
            found = True
        # Increment j
        j += 1

    print "The smallest odd composite number that cannot be decomposed"
    print "  into a prime plus twice a square is: %d" % (oc)
