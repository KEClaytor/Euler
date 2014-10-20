# Cubic permutations
# Find the smallest cube where five permutations
#  of it's digits are also cubes

from itertools import permutations
from eulermath import array2int, int2array, nintdigits, dropsmallint
from math import floor, ceil

# They may not be exactly equal due to floating point
# But if we round to the closest int and cube it
#  we should get back to the start
def iscube(testint):
    # NOTE: Don't use int for raw conversion
    #       Round first to avoid truncation errors
    cr = round(testint**(1/3.0))
    return (int(round(cr**3)) == testint)

def getcubicperms(myint):
    cps = []
    perm = list(set(map(array2int, permutations(int2array(myint)))))
    perm = dropsmallint(perm, nintdigits(myint)-1)
    for p in perm:
        if iscube(p):
            cr = int( round(p**(1/3.0)) )
            cps.append(cr)
    return list(set(cps))

if __name__ == "__main__":
    #print iscube(41063625)     # Test subfunction
    #mylist = [340, 345]        # Test list
    mylist = range(1,1000)
    skip = []
    for myint in mylist:
        if myint not in skip:
            cube = myint**3
            cps = getcubicperms(cube)
            n = len(cps)
            # Keep the user informed
            if n > 1:
                print myint, cube, cps
                print "%d = %d^3 has %d cubic permutations" % (cube, myint, n)
                for x in cps:
                    skip.append(x)
            if n == 5:
                break
