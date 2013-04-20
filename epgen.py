# A prime list generator for Project Euler problems
# This script adds primes to the list stored in file;
#  'eplist.dat'

from eulermath import isprime
# Load up the list and see what the last prime that we added was

# Begin adding primes from that value on.
n = 3
while (n < 1000):
    if(isprime(n) == 1):
        print n
    n += 2
# Puzzle Thomas gave me:
#form 24 out of 1, 3, 4, 6
#4*6 = 24
#1+3 = 4
#3*4 = 12
#6*7 = 42
#6-1 = 5 * 4 = 20 + 3 = 23
#4*4 = 16 + 6 = 22
