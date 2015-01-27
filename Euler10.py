from eulermath import isprime

if __name__ == "__main__":
    # Test case, should give 17
    # nmax = 10
    nmax = 2000000
    total = 2
    n = 3
    while (n < nmax):
        if (isprime(n) == 1):
            total += n
        n += 2

    print "The sum of primes below", nmax, "is", total
