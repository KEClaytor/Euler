import sys
from eulermath import isprime 
#n = 10
#n = 13195 #should give 29
n = 600851475143
x = 2
while (x < n/2):
    #for x in range(n-1,n/2,-1):
    #print "is", x, "a factor?"
    if n % x == 0:
        # This is a factor check if it is prime
        b = n/x
        c = isprime(b)
        print "testing number:", b, c 
        if c == 1:
            # We are a prime number
            # Since we are going from large numbers
            #   To small, this must be the largst prime
            print "The largest prime factor of", n, "is", b
            break
    x += 1

