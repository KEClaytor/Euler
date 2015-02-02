# Find the sum of the digits in the numerator
#  for the 100th convergent of the continued
#  fraction for e

from fractions import Fraction
from eulermath import int2array, frac2str, makecontfrac


def convterms_e(n):
    enot = [0]*n
    for x in range(n):
        if x == 0:
            enot[x] = 2
        elif (x+2) % 3 == 1:
            enot[x] = 2*((x+2)/3)
        else:
            enot[x] = 1
    return enot

if __name__ == "__main__":
    print convterms_e(10)
    print makecontfrac(convterms_e(10))
    t100 = makecontfrac(convterms_e(100))
    snd = sum(int2array(t100.numerator))
    print ("The sum of the digits in the numerator of the " +
           "100th convergent of e is: %d" % (snd))
