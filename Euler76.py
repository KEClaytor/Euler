# The same as the coinage problem
from eulermath import coinage

print "Check: %d ways to write 5 as the sum of >=2 ints." % ( coinage(5,range(1,5)) )
print "Solution: %d ways to write 100 as the sum of >=2 ints." % ( coinage(100,range(1,100)) )
