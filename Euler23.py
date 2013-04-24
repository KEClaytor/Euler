# Find the sum of numbers that cannnot be written as
#                      the sum of two abundant numbers
from eulermath import factors

# Check to see if a number is abundant
def isabundant(num):
	isab = 0
	fac = factors(num)
	fac.pop()	# remove the number itself from the list
	if (sum(fac) > num ):
		isab = 1
	return isab

# If two numbers from the abundant list sum to our value
#  then it is the sum of two from the ablist
def issum(num,ablist):
	issum = 0
	# Make sure that ablist is populated
	if ablist:
		for x in ablist:
			y = num-x
			if y in ablist:
				issum = 1
				break
	return issum

# Some debugging
testlist = [12,28]
for n in testlist:
	print "Is "+repr(n)+" abundant?: "+repr(isabundant(n))

# Loop through to the given max bound
# (see the problem for a more consice way of stating this)
# Keep a list going of our abundant numbers
# and a running total of the sum
ablist = []
rtotal = 0
for x in xrange(1,28123):
	if isabundant(x):
		ablist.append(x)
	if not issum(x,ablist):
		rtotal += x
		#print repr(x) +"is a sum of abundant numbers. Current total: "+repr(rtotal)

print "Total of numbers < 28123 that cannot be expressed as a sum of abundant numbers is: "+repr(rtotal)
