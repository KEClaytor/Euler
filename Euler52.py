# Find the first number x such that
#  2x, 3x, 4x, 5x, and 6x all contain the same digits

from eulermath import int2array

def checkdigits(t):
    check = 0
    ar = int2array(t[0])
    br = int2array(t[1])
    ar.sort()
    br.sort()
    if len(ar) == len(br):
        for ii in range(len(ar)):
            if ar[ii] != br[ii]:
                break
            if ii == len(ar)-1:
                check = 1 
    return check

found = 0
test = 0
while not found:
    test += 1
    multiples = [test*n for n in range(1,6)]
    result = map(checkdigits, zip([test]*6,multiples))
    if sum(result) == len(result):
        found = 1

print "%d is the first number that contains the same digits as 1-6*%d" % (test,test)

