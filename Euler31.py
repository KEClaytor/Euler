# The coin change problem can be solved by the help of generating functions
#  from combinatorics
# The ways of making change for p cents is the coefficient of x^p in
#  expanding; 1/((1 - x)(1 - x^5)(1 - x^10)...(1 - x^largestchange))
# For the reasoning, let's take the simple example of making change using
#  only 5c pieces, we have 1 way of making zero cents, 1 way of making 5c, ...
# Hence; 1 + x^5 + x^10 + x^15 = 1/(1 - x^5)
# We multiply by the generating functions for other coin denominations
#  to obtain the above sequence. I'll implement this method for finding that
#  coefficient;
# http://math.stackexchange.com/questions/176363/keep-getting-generating-function-wrong/176397#176397
import array

amt = 200
coins = [1,2,5,10,20,50,100,200]
c = array.array('i',(0,)*(amt+1))
c[0] = 1

for k in coins:
    for i in range(amt-k+1):
        c[i+k] += c[i]

print "There are " +str(c[12]) + " ways to make change for 12c, and"
print str(c[200]) + " ways to make change for 200c using euroinas."
        
