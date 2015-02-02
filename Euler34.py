import math
from eulermath import int2array


# Applies the factorial to each element in a list
def facArray(arr):
    newarr = []
    for i in arr:
        newarr.append(math.factorial(i))
    return newarr

if __name__ == "__main__":
    # Find the upper bound we need to go to
    for ii in range(2, 10):
        ninestr = int("9"*ii)
        ninetotal = sum(facArray(int2array(ninestr)))
        if (ninetotal < ninestr):
            print "max bound = ", ninestr
            nmax = ninestr
            break

    totalsum = 0
    n = 3
    while (n < nmax):
        intarr = int2array(n)
        intsum = sum(facArray(intarr))
        if intsum == n:
            print intsum
            totalsum += intsum
        n += 1

    print ("The sum of numbers that are the sum of " +
           "the factorials of their digits is:", totalsum)
