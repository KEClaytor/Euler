# n-digit numbers which are a number to the nth power
#  eg; 16807=7^5 is a 5-digit number
from eulermath import int2array
from math import floor, ceil

# total = 0
# # They seem to cap off after 21, but we'll go to 100 just in case
# for power in range(1, 100):
#     #print "Testing new power: %d" % (power)
#     for base in range(1, 100):
#         ndigits = len(int2array(base**power))
#         if ndigits == power:
#             print ("%d^%d = %d (%d digits)" %
#                    (base, power, base**power, ndigits))
#             total += 1
#
# print "Total number of positive intgers with this property: %d" % (total)


# A more elegant solution
def lowval(n_digits):
    val = '1'
    for jj in range(n_digits-1):
        val += '0'
    return int(val)


def highval(n_digits):
    val = ''
    for jj in range(n_digits):
        val += '9'
    return int(val)

if __name__ == "__main__":
    total = 0
    for power in range(1, 100):
        base_min = ceil(((lowval(power)))**(1./power))
        base_max = floor(((highval(power)))**(1./power))
        nbetween = base_max - base_min + 1
        print power, base_min, base_max, nbetween
        total += nbetween
        if base_min > base_max:
            break

    print "Total number of positive intgers with this property: %d" % (total)
