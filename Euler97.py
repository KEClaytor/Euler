# Find the last 10 digits of a large non-Mersenne prime

from eulermath import int2array, array2int


# Returns the last ndigits of a number
def lastdigits(num, ndigits):
    arr = int2array(num)
    return array2int(arr[-ndigits::])

if __name__ == "__main__":
    # The equation for the prime is;
    # 28433*2**7830457+1
    # We're only interested in the last 10 digits
    power = 7830457
    mult = 28433
    add = 1
    digits = 10

    base = 2
    val = 1
    for x in range(1, power+1):
        val = val*base
        val = lastdigits(val, digits)
        # print val
        # if x%(power/10)==0:
        #     print "+10%"

    # Multiply and add
    val = mult*val + add
    val = lastdigits(val, digits)

    print "The last 10 digits are: %d" % (val)
