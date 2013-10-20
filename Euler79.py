# Passcode derivation: a subgroup of
#   three digits is drawn from a longer passcode;
#   eg; 531278 -> 317

# From successful logins rebuild
#   the password of unknown length
from eulermath import int2array, array2int, hist

# Quick 2-level flatten
flatten = lambda arr: [x for l in arr for x in l]

# Test to see if the elments of two lists are equal
def listeq(a,b):
    eq = False
    if len(a) == len(b):
        eq = True
        for ii in range(len(a)):
            if a[ii] != b[ii]:
                eq = False
                break
    return eq

# Check that the list test can generate the observed keys
def checkval(test,keys):
    check = True
    for key in keys:
        ind = []
        for x in key:
            ind.append(test.index(x))
        if not listeq(ind,ind.sort()):
            check = False
            break
    return check

# Trim values based on frequency
# totrim is a tuple of lists, and counts is a list
#  all these lists must be the same length
def trim(totrim,counts,minv=0,maxv="inf"):
    trimmed = []
    for slist in totrim:
        tsublist = []
        for ii in range(len(counts)):
            cnt = counts[ii]
            if (cnt>minv) and (cnt<maxv):
                tsublist.append(slist[ii])
        trimmed.append(tsublist)
    return trimmed

# Make some potential keys
def make_potential_keys(start=0,end=0,midpairs=[00]):
    potential_keys = make_potential_keys(start=7,end=0,midpairs=flatten([t12[0],t23[0]]))
    
# Import the data
sub = []
p12 = []; p23 = []
p1 = []; p2 = []; p3 = []
fnames = open('Euler79.dat')
for line in fnames:
    val = int2array(int(line))
    # All values
    sub.append(val)
    # Single values
    p1.append(val[0])
    p2.append(val[1])
    p3.append(val[2])
    # Pairs
    p12.append(array2int(val[0:2]))
    p23.append(array2int(val[1:3]))

# Flatten out the sublist and take all unique elements
fsl = list(set([x for arr in sub for x in arr]))
# this length is the shortest password size

v1, c1 = hist(p1)
v2, c2 = hist(p2)
v3, c3 = hist(p3)
v12, c12 = hist(p12)
v23, c23 = hist(p23)

print fsl
print trim([v1,c1],c1,2)
print trim([v2,c2],c2,2)
print trim([v3,c3],c3,2)
print trim([v12,c12],c12,2)
print trim([v23,c23],c23,2)
# Looking at the histograms, we can see
#   that there are a few numbers;
#    7 - which appears most frequently in the
#        first column, but not in the second
#    0 - which appears second most frequently
#        in the thrid column, but not in the second

# These are the likely ending numbers
# We will then have to sort the others based on their pairs

t12 = trim([v12,c12],c12,2)
t23 = trim([v23,c23],c23,2)
potential_keys = make_potential_keys(start=7,end=0,midpairs=flatten([t12[0],t23[0]]))

print potential_keys

