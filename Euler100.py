# Find the number of blue disks such that
#  the probability of obtaining two blue disks
#  on random draws is exactly 1/2
# Note: we're dealing with integer disks

# We'll be solving:
# (b)*(b-1)       1
# ------------- = -
# (r+b)*(r+b-1)   2

# We can find a guess for b by noticing that with r+b is large
#  2b^2 - 2b - (r+b)^2 ~= 0

# With this, we can cycle over the sum values and find b
#  with the quadratic formula

# Call s^2 = (r+b)*(r+b-1), then;
#      1 +/- sqrt(1+2s^2)
#  b = -----------------
#             2
# Since s > 10^12; 1 << s, and
#  sqrt(1+2s^2) ~= sqrt(2)s
# And b ~= s/sqrt(2)
from math import ceil, floor


def test(b, s):
    return 2*b*(b-1) == s*(s-1)

for jj in xrange(10000000):
    s = int(10**12 + jj)
    b_float = s / (2**0.5)
    b_lower = int(floor(b_float))
    b_upper = int(ceil(b_float))
    if test(b_lower, s):
        print b_lower, s
    if test(b_upper, s):
        print b_upper, s
