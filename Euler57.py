# How many fractions contain a numerator with more digits
#   than the denominator in the decimal fraction expansion
#   of sqrt(2)

from fractions import Fraction
from eulermath import int2array, frac2str


def haslongnum(frac):
    ln = 0
    if len(int2array(frac.numerator)) > len(int2array(frac.denominator)):
        ln = 1
    return ln


# Returns with the next term in the decimal expansion of sqrt(2)
def nextterm(lastterm):
    nextterm = 1 + 1/(lastterm+1)
    return nextterm

if __name__ == "__main__":
    # Number with a longer numerator
    nt = Fraction(1, 1)
    nln = 0
    for x in range(1000):
        nt = nextterm(nt)
        # print "%s | %d" % (frac2str(nt), haslongnum(nt))
        if haslongnum(nt):
            nln += 1

    print ("In the first 1000 of sqrt(2) %d contain a " +
           "numerator longer than the denominator." % (nln))
