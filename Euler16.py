from eulermath import int2array

#nexp = 15 # Test case, should give 26
nexp = 1000

print "The sum of the digits in 2^", nexp, "is:", sum(int2array(2**nexp))
