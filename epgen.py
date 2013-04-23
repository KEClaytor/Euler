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
while (nadded < 1000):
    if(isprime(n) == 1):
		pfile.write(str(n))
		pfile.write('\n')
		nadded += 1
    n += 2

# Puzzle Thomas gave me:
#form 24 out of 1, 3, 4, 6
#4*6 = 24
#1+3 = 4
#3*4 = 12
#6*7 = 42
#6-1 = 5 * 4 = 20 + 3 = 23
#4*4 = 16 + 6 = 22
