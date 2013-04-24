# Truncatable primes
from eulermath import int2array
from eulermath import array2int
from eulermath import isprime
from eulermath import isprimelist
# Example case 3797 is truncatable from left to right
# 3797, 797, 97, and 7. From right to left: 3797, 379, 37, and 3.
# 

# Our truncation classes
def truncateLR(num):
	arr = int2array(num)
	arr.pop(0)
	tnum = array2int(arr)
	return tnum

def truncateRL(num):
	arr = int2array(num)
	arr.pop()
	tnum = array2int(arr)
	return tnum

# Checks to see if the value is a truncatable prime
def istruncprime(n):
	istp = 0
	if (n > 10 and isprime(n)):
		istplr = 1
		istprl = 1
		# if we have two digits we can pop another off
		nt = n
		while nt > 10:
			nt = truncateLR(nt)
			#print "nt: " + repr(nt) + "  prime: " + repr(isprime(nt))
			if (isprime(nt)==0):
				istplr = 0
				break
		if (istplr == 1):
			nt = n
			while nt > 10:
				nt = truncateRL(nt)
				#print "nt: " + repr(nt) + "  prime: " + repr(isprime(nt))
				if (isprime(nt)==0):
					istprl = 0
					break
		if (istplr and istprl):
			istp = 1
	return istp

# Start generating truncatable primes from the possible list of single digit primes
bp = ['2','3','5','7','9']
nl = bp

tprimes = []
while (len(tprimes) < 11):
	nl = [x+y for x in nl for y in bp]
	print nl
	for x in nl:
		testval = int(x)
		if istruncprime(testval):
			print "Found one: " + repr(testval)
			tprimes.append(testval)
	
print tprimes
print "The sum of the truncatable primes is: " + repr(sum(tlist))




