from eulermath import nCr
# Check that our nCr is working correctly
# by printing out the first few layers of pascal's triangle
for n in range(1,5):
    row = []
    for r in range(0,n+1):
        print "(",n,",",r,")"
        row.append(nCr(n,r))
    print row

# The solution to this problem is;
# Find the center element to row 2*n
#  For example, for a 2x2 it is the center element of row 4
#  1 4 6 4 1  => is 6
#nsides = 2 # Test case should give 6
nsides = 20

level = 2*nsides
print "There are", nCr(level,level/2), "routes through a grid of boxes", nsides, "to a side."
