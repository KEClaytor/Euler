from eulermath import isprime

if __name__ == "main":
    # Start looking for primes at 3 - skip all the
    # evens because they are not prime
    # test case, the 10th prime is 29
    # findpri = 10
    findpri = 10001
    indpri = 2   # The number of the prime we are - last found was 2
    cint = 3     # Current integer to test for prime-ness
    while (indpri < findpri):
        cint += 2
        # print "testing", cint, isprime(cint)
        if isprime(cint) == 1:
            indpri += 1

    print "The", indpri, "th prime is:", cint
