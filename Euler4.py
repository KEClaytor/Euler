import math
from eulermath import int2intarray

# Function that checks a list to see if it is a palindrome
def ispalindrome(plist):
    #Create a reversed copy of our list
    rlist = plist[:]
    rlist.reverse()
    ispal = 1
    # Loop through elements
    for x in range(0,len(plist)/2):
        if (plist[x] != rlist[x]):
            ispal = 0
            break
    return ispal

#n = 99 # Test case, should give 9009
n = 999
largest = 0
for ii in range(0,n):
    for jj in range(0,n):
        prod = (n-ii)*(n-jj)
        # If we are a palindrome see if we're larger
        if (ispalindrome(int2array(prod)) == 1):
            if (prod > largest):
                largest = prod

print "The largest product of numbers less than", n, "that is a palindrome is:", largest
