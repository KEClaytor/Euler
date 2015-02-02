# Find the prime < 1M that can be written as the sum
#  of the most consecutive primes

from eulermath import isprime

if __name__ == "__main__":
    maxp = 10**6
    # Import a list of the primes < 1M
    prime_sm = []
    pfile = open("eplist.dat")
    for line in pfile:
        prime = int(line)
        if prime >= maxp:
            break
        else:
            prime_sm.append(prime)

    maxsum = 2
    maxlen = 1
    maxseq = []
    for jj in range(len(prime_sm)):
        for ii in range(jj):
            seq = prime_sm[ii:jj]
            seqsum = sum(seq)
            if (seqsum < maxp):
                if (isprime(seqsum)) and (len(seq) > maxlen):
                    maxsum = seqsum
                    maxlen = len(seq)
                    maxseq = seq
            else:   # we have exceeded the 1M mark
                break

    print maxsum
    print maxlen
    print maxseq
