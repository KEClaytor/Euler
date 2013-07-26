# n-digit numbers which are a number to the nth power
#  eg; 16807=7^5 is a 5-digit number
from eulermath import int2array

total = 0
# They seem to cap off after 21, but we'll go to 100 just in case
for power in range(1,100):
    #print "Testing new power: %d" % (power)
    for base in range(1,100):
        ndigits = len(int2array(base**power))
        if ndigits == power:
            print "%d^%d = %d (%d digits)" % (base,power,base**power,ndigits)
            total += 1

print "Total number of positive intgers with this property: %d" % (total)
