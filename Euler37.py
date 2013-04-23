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
		
print "Some test cases:"
print "  Is 3797 a truncatable prime?: " + repr(istruncprime(3797))
print "  Is 7 a truncatable prime?: " + repr(istruncprime(7))
print "  Is 47 a truncatable prime?: " + repr(istruncprime(47))

# Start going through our prime list
# Until we have found 11 truncatable primes
# And return their sum
pfile = open("eplist.dat")

plist = []
for line in pfile:
	ptest = int(line)
	if (ptest > 10):
		if istruncprime(ptest):
			print "Found a truncatable prime: " + repr(ptest)
			plist.append(ptest)
		if (len(plist) == 11):
			break
print "The sum of the truncatable primes is: " + repr(sum(plist))

