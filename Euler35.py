from eulermath import isprime
from eulermath import intcpermute

# print intcpermute(123)
# print isprime(4)

if __name__ == "__main__":
    # nmax = 100 # Test case, shoud give 13
    nmax = 1000000

    n = 2
    ncpri = 0
    prilist = []
    while n < nmax:
        if n % 100000 == 0:
            print "+10%"
        if isprime(n):
            for x in intcpermute(n):
                if isprime(x) != 1:
                    break
            else:
                ncpri += 1
                prilist.append(n)
        n += 1

    print "There are:", ncpri, "circular primes below", nmax
    # print prilist
