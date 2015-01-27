

# A function that returns the sequence
def sequence(n):
    seq = [n]
    while n > 1:
        if (n % 2 == 0):
            n = n/2
        else:
            n = n*3 + 1
        seq.append(n)
    return seq

if __name__ == "__main__":
    # Test case
    print sequence(13)

    nmax = 1000000
    longest = 0
    longeststart = 0
    for x in xrange(1, nmax+1):
        clen = len(sequence(x))
        if (clen > longest):
            longest = clen
            longeststart = x

    print "The longest length started with",
    longeststart, "and is length:", longest
