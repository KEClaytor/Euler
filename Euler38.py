# Finding the largest 1-9 pandigital that is formed by concatenating
#  an integer with (1,2,3,...,n) n>1

from eulermath import makepandigital, array2int


# Returns 0 if it does not form a concatenated product of
#  exactly maxlen, otherwise it returns the concatenated
#  product (this restriction is relaxed if soft = True)
def makecatprod(start, maxlen, soft=False):
    rval = 0
    num = ''
    seq = [start]
    mult = 2
    while len(num) < maxlen:
        seq.append(start*mult)
        num = ''.join([str(val) for val in seq])
        mult += 1
    if soft:
        rval = int(num[0:maxlen])
    else:
        if len(num) == maxlen:
            rval = int(num)
    return rval


# Takes in a pandigital number and determines if it can
#  be formed by concatenating the product of an integer
# We do this by taking the first n digits, and multiplying
#  them by the sequence (1,2,3,4,...) until we have a
#  9 digit number, then we can compare that
def findpancat(pan):
    rval = 0
    ipan = array2int(pan)
    # We only need to search for something < 5 digits
    for ii in range(1, 6):
        start = array2int(pan[0:ii])
        cprod = makecatprod(start, 9)
        if cprod == ipan:
            rval = 1
    return rval

if __name__ == "__main__":
    plist = makepandigital(9, True)
    for pan in plist:
        findpancat(pan)
        if findpancat(pan):
            print ("The largest pandigital that can be formed " +
                   "as a concatenated product is: %d" % (array2int(pan)))
            break
