from eulermath import factors

if __name__ == "__main__":
    # Test case, 7th triangle number is 28 and is the first to have > 5 factors
    # fmax = 5
    fmax = 500
    i = 1
    # print "i  tri"
    while True:
        # What is the corresponding triangle number
        tri = sum(range(1, i))
        nfac = len(factors(tri))
        # print i, tri, factors(tri)
        if (nfac > fmax):
            break
        i += 1

    print "The first triangle number to have over", fmax, "factors is:", tri
