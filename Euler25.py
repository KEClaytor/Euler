from eulermath import int2array

if __name__ == "__main__":
    # ndigmax = 3 # Test case, should give the 12th term, 144
    ndigmax = 1000

    ndigs = 1
    a = 1
    b = 1
    n = 2  # Current term number
    while (ndigs < ndigmax):
        nb = b + a
        a = b
        b = nb
        n += 1
        ndigs = len(int2array(b))
        # print n, b

    print "The first term to have over", ndigmax,
    "digits is the", n, "th term = ", b
