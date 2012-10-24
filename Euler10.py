# Returns 0 for nonprime, and 1 for prime
def isprime(n):
    prime = 1
    x = 2
    while (x < n/2):
        if n % x == 0:
            prime = 0 
            break
        x += 1
    return prime 

#nmax = 10 # test case, sum of primes below this = 17
nmax = 2000000
total = 2
n = 3
while (n < nmax):
    if (isprime(n) == 1):
        total += n
    n += 2

print "The sum of primes below", nmax, "is", total
