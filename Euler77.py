from eulermath import coinage

# Very similar to the coinage probelm (Euler31)
# We want to write a number as combinations of sums of primes smaller
#  than itself. What is the first number to have over 5000 ways of
#  writing it usnig this condition?

# Start with 3, read the primes off of our prime list and use these
#  to make the list of prime 'coins'. Then use coinage to cout the ways
pfile = open("eplist.dat")

plist = []
n = 3
nways = 0
for line in pfile:
    cprime = int(line)
    while (n <= cprime):
        nways = coinage(n, plist)
        if (nways > 5000):
            print (repr(n) + " is the first value that can be " +
                   "written as a sum of primes in more than 5000 ways.")
            break
        n += 1
    # Check again with our condition - there has to be a better way for this...
    if (nways > 5000):
        break
        # Debugging
        # print ("Value: " + repr(n) + " has " + repr(nways) +
        #        " ways of being written with smaller primes.")
    plist.append(cprime)
