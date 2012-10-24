# 2520 is the samllest that is evenly divided by 1 through 10
# What about 1 through 20?

#divisors = range(1,11) # Test case, should give 2520
divisors = range(1,21) # Real case
print "Testing for division by:", divisors
print "Moving in chunks of:", divisors[-1]

# pick a starting point
n = 2000
success = 0

while (success == 0):
    # We know that the value must be evenly divisible
    #  by the last element in the list, so move by those steps
    n += divisors[-1] 
    for x in divisors:
        if n % x != 0:
            break
    else:
        # we have found a number that is
        #   evenly divisible by all divisors
        success = 1
print "Success! The number is:", n
