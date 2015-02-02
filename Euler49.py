# Find the one other sequence of 4-digit permuted increasing primes
#  The first is; 1487, 4817, 8147 (difference is 3330)
from eulermath import (isprime, int2array, array2int,
                       find_primes_in_list, find_arithemetric_series)
from itertools import permutations, combinations

if __name__ == "__main__":
    # Start by finding all 4-digit primes
    print "Finding arithemetric series of primes between 1001 and 9999:"
    exclude = []
    for trial in xrange(1001, 9999, 2):
        if trial not in exclude:
            if isprime(trial):
                # Find the permutations of this number
                tp = permutations(int2array(trial))
                # Get the unique values and sort them
                tpl = list(set([array2int(x) for x in tp]))
                tpp = find_primes_in_list(tpl)
                tpn = []
                for x in tpp:
                    if x > 1000:
                        tpn.append(x)
                # Exclude the others
                for p in tpn:
                    exclude.append(p)
                # Find any arithemetric series of length 3 in the prime list
                aseries = find_arithemetric_series(tpn, 3)
                if len(aseries) > 0:
                    print aseries
                    for series in aseries:
                        print series
                        cat = ''.join(str(elem) for elem in series)
                        print "As a string: " + cat
