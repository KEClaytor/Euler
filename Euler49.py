# Find the one other sequence of 4-digit permuted increasing primes
#  The first is; 1487, 4817, 8147 (difference is 3330)
from eulermath import isprime, array2int, int2array, arraydiff
from itertools import permutations

def find_primes_in_perm(perm_list):
    prime_list = []
    for x in perm_list:
        val = array2int(x)
        if isprime(val) and val>1000:
            prime_list.append(val)
    return list(set(prime_list))
 
exclude = []
# Start by finding all 4-digit primes
for trial in xrange(1001,9999,2):
    if trial not in exclude:
        if isprime(trial):
            # See if the prime has at least 2 permutations amongst the set
            tp = permutations(int2array(trial))
            tp.next() # we don't need to try ourself
            tpp = find_primes_in_perm(tp)
            if len(tpp) == 3:
                #for x in tpp:
                #    print x
                tpp.sort()
                diff_vec = list(set(arraydiff(tpp)))
                diff_length = len(diff_vec)
                if diff_length == 1:
                    print ""
                    print "Found a group of 3"
                    print tpp
                    print diff_vec
                    print "length = %d" % (diff_length)
            # And skip the others

