# append decimal fraction created by concatenating the positive intergers
# 0.1234567891011121314151617181920...
from __future__ import division
import math


# Returs the number of terms in a specific order of magnitude
# eg, mag = 1 is 1,2,3,4,5,6,7,8,9 = 9 terms = 9 letters
#     mag = 2 is 1,2,...10,11,12,...98,99 = 180
#           (90 #'s from 10-99 * 2chars) + 9chars (1-9)
def termsinmag(mag):
    if mag == 0:
        addterms = 0
    else:
        addterms = mag*(9*10**(mag-1)) + termsinmag(mag-1)
    return addterms


# Function that determines the nth digit of the series
def dn(n):
    mag = 1  # Order of magnitude counter
    while n > termsinmag(mag):
        mag += 1
    # print ("n = " + repr(n) + " mag = " + repr(mag) +
    #        " tim = " + repr(termsinmag(mag-1)))
    rn = n - termsinmag(mag-1)
    num = (math.ceil(rn/mag)-1) + 10**(mag-1)
    dig = str(num)
    # print "rn = " + repr(rn) + " num = " + repr(num)
    if mag == 1:
        rchar = dig[0]
    else:
        rchar = dig[(rn-1) % mag]
    return rchar

# print "Start:"
# for ii in range(1,5):
#     print "new val:"
#     print termsinmag(ii)
#  Test case, print out the first p digits of the series
# p=200
# seq = []
# for n in range(1,p):
#     seq.append(dn(n))
# print ''.join(seq)
# print dn(12)

if __name__ == "__main__":
    pmax = 6
    prod = 1
    for x in range(pmax+1):
        print "dn(10^"+repr(x)+") = " + repr(dn(10**x))
        prod *= int(dn(10**x))

    print "dn(1) * dn(10) * --- * dn(10^"+repr(pmax)+") = " + repr(prod)
