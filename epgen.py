# A prime list generator for Project Euler problems
# This script adds primes to the list stored in file;
#  'eplist.dat'

from eulermath import isprime
# Load up the list and see what the last prime that we added was
# Make sure that we can write the file later
pfile = open("eplist.dat","r+")
for line in pfile:
    pass
lastprime = int(line)

# Begin adding primes from that value on.
n = lastprime+2
nadded = 0
while (nadded < 10000):
    if(isprime(n) == 1):
        print "Found another: " + repr(n)
        pfile.write(str(n))
        pfile.write('\n')
        nadded += 1
    n += 2

