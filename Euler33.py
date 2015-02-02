# Digit cancelling fractions
# Fake cancelling options eg 49/98 = 4/8
# Ignore the trivial cases of 30/50 = 3/5
# Considering only two digit fractions < 1
# There should be 4 non-trivial cases

# Start by looping through all the numbers < 99
# The look at the smaller numbers that contain
#  one of those digits, this way we know we
#  have a possible digit cancelling and we satisify
#  the < 1 condition
from __future__ import division
import fractions

if __name__ == "__main__":
    pdenom = 1
    pnumer = 1
    for denom in range(10, 99):
        # For each digit come up with a numerator
        # that contains that digit
        # Ignore the case where our non-truncated digit is zero.
        if (denom % 10 != 0):
            dig1 = int(str(denom)[0])
            dig2 = int(str(denom)[1])
            # Ignore a leading zero, and a trailing zero
            for digx in range(1, 9):
                numer1 = 10*dig1 + digx
                numer2 = 10*digx + dig1
                if (numer1 != denom) and (numer1/denom == digx/dig2):
                    print "Numer1 = " + repr(numer1)
                    print "%2d / %2d = %2d" % (numer1, denom, numer1/denom)
                    print "%2d / %2d = %2d" % (digx, dig2, digx/dig2)
                    pnumer = pnumer*numer1
                    pdenom = pdenom*denom
                if (numer2 != denom) and (numer2/denom == digx/dig2):
                    print "Numer2 = " + repr(numer2)
                    print "%2d / %2d = %2d" % (numer2, denom, numer2/denom)
                    print "%2d / %2d = %2d" % (digx, dig2, digx/dig2)
                    pnumer = pnumer*numer2
                    pdenom = pdenom*denom

    print "Product of fractions:"
    print repr(pnumer) + "/" + repr(pdenom)
    gcd = fractions.gcd(pnumer, pdenom)
    print "Reduced form:"
    print repr(pnumer/gcd) + "/" + repr(pdenom/gcd)
