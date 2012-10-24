import math
from eulermath import factors

# Checks to see if a pair of numbers is amicable and return both
def isamicable(n):
    pair = []
    nfac = factors(n)
    nfac.pop() # Remove the number itself
    dn = sum(nfac)
    dnfac = factors(dn)
    dnfac.pop()
    dnp = sum(dnfac)
    #print n, dn, dnp
    if (dnp == n):
        pair.append(n)
        pair.append(dn)
    return pair

# Test case, should return [220,284]
print isamicable(220)
print isamicable(6)
print isamicable(28)
print isamicable(496)
print isamicable(2620)
print isamicable(8128)

# Loop through the numbers < 10000
# And search for amicable pairs
nmax = 10000
allpairs = []
for n in xrange(2,nmax+1):
    cpair = isamicable(n)
    # Leave out self-amicable numbers
    if (len(cpair) > 0):
        if (cpair[0] != cpair[1]):
            allpairs.append(cpair[0])
            allpairs.append(cpair[1])

#print allpairs

# We will have duplicates so sorth these out before we sum
sorted_no_duplicates = list(set(allpairs))
sorted_no_duplicates.sort()
totalamsum = sum(sorted_no_duplicates)

print "The sum of all amicable pairs under", nmax, "is:", totalamsum
