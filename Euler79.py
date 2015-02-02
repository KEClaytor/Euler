# Passcode derivation: a subgroup of
#   three digits is drawn from a longer passcode;
#   eg; 531278 -> 317

# From successful logins rebuild
#   the password of unknown length
from eulermath import int2array, array2int, hist

# Quick 2-level flatten
flatten = lambda arr: [x for l in arr for x in l]


# Trim values based on frequency
# totrim is a tuple of lists, and counts is a list
#  all these lists must be the same length
def trim(totrim, counts, minv=0, maxv="inf"):
    trimmed = []
    for slist in totrim:
        tsublist = []
        for ii in range(len(counts)):
            cnt = counts[ii]
            if (cnt > minv) and (cnt < maxv):
                tsublist.append(slist[ii])
        trimmed.append(tsublist)
    return trimmed

if __name__ == "__main__":
    # Import the data
    sub = []
    p123 = []
    p12 = []
    p23 = []
    p1 = []
    p2 = []
    p3 = []
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
        p123.append(array2int(val))

    # Flatten out the sublist and take all unique elements
    fsl = list(set([x for arr in sub for x in arr]))
    # this length is the shortest password size

    v1, c1 = hist(p1)
    v2, c2 = hist(p2)
    v3, c3 = hist(p3)
    v12, c12 = hist(p12)
    v23, c23 = hist(p23)
    v123, c123 = hist(p123)

    print "We need to use all these:"
    print fsl
    print "max histograms"
    print trim([v1, c1], c1, 2)
    print trim([v2, c2], c2, 2)
    print trim([v3, c3], c3, 2)
    print trim([v12, c12], c12, 2)
    print trim([v23, c23], c23, 2)
    print "all histograms"
    print [v1, c1]
    print [v2, c2]
    print [v3, c3]
    print [v12, c12]
    print [v12, c12]
    print [v23, c23]
    print [v123, c123]
    # Looking at the histograms, we can see
    #   that there are a few numbers;
    #    7 - which appears most frequently in the
    #        first column, but not in the second
    #    0 - which appears second most frequently
    #        in the thrid column, but not in the second

    # These are the likely ending numbers
    # We will then have to sort the others based on their pairs

    print "Now stare at this histograms... "
    print "7 and 0 pretty obviously begin and end."
    print "3 is 2nd spot, as it never is chosen as an end..."
    print "and 9 is the second to last as it never begins."
    print "the work through the other options..."
    print "62 appears and 26 never does..."
    print "...scratch head..."
    print
    print "and discover the answer; 73162890"
