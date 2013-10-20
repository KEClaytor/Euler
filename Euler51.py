# If you replace digits in a prime
#  find an 8 prime family.

# Modified from Euler36
from Euler36 import make_palindrome_half
from eulermath import int2array, array2int, primesieve

# Replaces the digits of the prime number
#  replacement digits contained in rd
def replaceprime(prime):
    findall = lambda my_list: [i for i, x in enumerate(my_list) if x == '1']
    ndig = len(int2array(prime))
    pgroup = []
    replacement_dig = make_palindrome_half(ndig-1)
    # Ignore the last replacement rule, it is '0000'
    for reprule in replacement_dig[:-1]:
        # Run replacement for all integers
        subgroup = []
        newprime = int2array(prime)
        for cint in range(10):
            for ind in findall(reprule):
                newprime[ind] = cint
            # Check that the length is the same
            if len(newprime) == len(int2array(array2int(newprime))):
                subgroup.append(array2int(newprime))
        pgroup.append(subgroup)
    return pgroup

if __name__ == "__main__":
    fam_test_size = 6
    # We have the solutions for a 6 and 7 family size, make sure we get these back
    print "Printing primes, family size, and minimum prime in family"
    print "Also printing full familly for check"
    for ndig in range(2,9):
        # We want these two to be discrete
        primes = list(primesieve(10**ndig))
        primescheck = set(primesieve(10**ndig))
        #print "Primes"
        #print primescheck
        for prime in primes:
            testlists = replaceprime(prime)
            #print "After replacement:"
            #print testlists
            for test in testlists:
                primes_in_test = primescheck.intersection(test)
                #print primes_in_test
                famsize = len(primes_in_test)
                #print "Prime and family size:"
                if famsize >= fam_test_size:
                    fam_test_size += 1
                    print
                    print prime, famsize, min(primes_in_test)
                    print primes_in_test
                # Remove other primes whose families we have found
                for ppop in primes_in_test:
                    try:
                        primes.pop(primes.index(ppop))
                    except ValueError:
                        continue
                
