from eulermath import isprime

#nmax = 10 # test case, sum of primes below this = 17
nmax = 2000000
total = 2
n = 3
while (n < nmax):
    if (isprime(n) == 1):
        total += n
    n += 2

print "The sum of primes below", nmax, "is", total
