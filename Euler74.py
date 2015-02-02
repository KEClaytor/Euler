# Number of chains below 1M with sixty terms.

from math import factorial
from eulermath import int2array

terminal = {169: 3, 363601: 3, 1454: 3, 871: 2,
            45361: 2, 872: 2, 45362: 2, 145: 1}


def nextterm(n):
    return sum(map(factorial, int2array(n)))

# The recursive algorithm doesn't seem to work for larger numbers
# def chainlength(n):
#     nt = nextterm(n)
#     if nt in terminal:
#         return 1 + terminal[nt]
#     else:
#         return 1 + chainlength(nt)


# Non-recursive, and uses a max chain length
# Because we're only interested in a max chain length of 60
# A chain length of 61 and 43253 has the same meaning (!=60)
def chainlength(n):
    cl = 1
    nt = nextterm(n)
    while (nt not in terminal) and (cl <= 60):
        nt = nextterm(nt)
        cl += 1
    if nt in terminal:
        cl += terminal[nt]
    return cl

if __name__ == "__main__":
    # Check that we get the proper chain lengths from the examples
    print "69's chain length should be 5: %d" % (chainlength(69))
    print "78's chain length should be 4: %d" % (chainlength(78))
    print "540's chain length should be 2: %d" % (chainlength(540))

    n60c = 0
    for n in range(1, 10**6):
        if chainlength(n) == 60:
            n60c += 1

    print "There are %d chains <1M whose lenth is 60 terms." % (n60c)
