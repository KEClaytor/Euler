# Sum the even values of the Fibonacci sequence
# Consider only terms < 4*10^6

# Brute force method

if __name__ == "main":
    # fmax = 90 # should give 44
    fmax = 4000000
    fibsum = 0

    # The starting values
    # Note that the third is always even
    fa = 1
    fb = 1
    fc = 2

    # print "Even terms in the Fib sequence are:", fa, fb, fc
    while (fc < fmax):
        fibsum += fc
        fa = fc + fb
        fb = fa + fc
        fc = fa + fb
        # print fa, fb, fc

    print "The sum of fibonacci numbers <", fmax, "is:", fibsum
