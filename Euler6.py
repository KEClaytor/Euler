#n = 10 # Test case, should give 2640
n = 100 # Full case

# Sum of the squares
# Use the square pyramidal number equation
ssq = (2*n**3 + 3*n**2 + n)/6
print "Sum of the squares = ", ssq

# Square of the sum
# For the sequence starting at 1 and incrementing by 1
# S = n(n+1)/2
sqs = (n*(n+1)/2)**2
print "Square the sums = ", sqs

# Difference
print "Difference = ", sqs-ssq


