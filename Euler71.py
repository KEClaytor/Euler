# Find the reduced proper fraction just smaller than 3/7 for a maximum denominator of 1,000,000

# ARGH current build doesn't have this
#from future import division
from eulermath import factors
from math import floor

def is_reduced_proper_fraction(num, denom):
    common_factors = set(factors(num)) & set(factors(denom))
    if len(common_factors) == 1:
        return True
    else:
        return False

def less_than_three_sevenths(num, denom):
    if num/denom < 3.0/7.0:
        return true
    else:
        return false

# Maximum denominator
maxd = 1000000.
closest_num = 0
closest_denom = 1

print "Searching with maximum denominator: %d" % (maxd)
# We can rely on condition evaluation order in python
for denom in xrange(maxd+1):
    # Evaluate this backwards until we find
    #  a reduced proper fraction < 3/7
    for num in range(floor(denom*3.0/7.0)):
        if is_reduced_proper_fraction(num, denom):
            closest_num = num
            closest_denom = denom
            print "Updating with %d/%d" % (num, denom)

print "The closest reduced proper fraction is %d/%d" % (closest_num, closest_denom)
