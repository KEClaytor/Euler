# Euler 60
# Find the list of five primes whereby one can take any two
#  and concatenate them in any order and obtain a prime.

from eulermath import isprimeFermat as isprime, gen_primes

if __name__=="__main__":
    primes = gen_primes()
    print primes
    # Hint: we'll be expanding this list
    sequence = [3, 7]
    for prime in primes:
        works = True
        for cp in sequence:
            cata = int(str(prime) + str(cp))
            catb = int(str(cp) + str(prime))
            if not isprime(cata) or not isprime(catb):
                works = False
        if works:
            sequence.append(prime)
            print sequence
        if len(sequence) == 5:
            break
    print "Found a length-5 sequence."
    print sequence, sum(sequence)
