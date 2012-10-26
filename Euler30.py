from eulermath import int2array

# Applies the power operator to each element in a list
def powArray(arr,mypow):
    newarr = []
    for i in arr:
        newarr.append(i**mypow)
    return newarr

#npow = 4 #Test case, should give 19316 = 1634 + 8208 + 9474
npow = 5
#nmax = 10**6 # Old upper bound, set arbitrarially
# Find the upper bound we need to go to
for ii in range(2,10):
    ninestr = int("9"*ii)
    ninetotal = sum(powArray(int2array(ninestr),npow))
    if (ninetotal < ninestr):
        print "max bound = ", ninestr
        nmax = ninestr
        break

totalsum = 0
n = 2
while (n < nmax):
    intarr = int2array(n)
    intsum = sum(powArray(intarr,npow))
    if intsum == n:
        print intsum
        totalsum += intsum
    n += 1

print "The sum of numbers that are the sum of the 5th power of their digits is:", totalsum
