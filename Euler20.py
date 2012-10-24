import math
from eulermath import int2array
#n = 10 # Test case, should give 27
n = 100

#print math.factorial(n)
myarray = int2array(math.factorial(n))
sumdigits = 0
#print myarray
for x in myarray:
    sumdigits += x

print "The sum of the digits of", (str(n)+"!") , "is:", sumdigits
