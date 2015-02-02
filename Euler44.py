# Search pentagonal numbers for where the sum and difference
#  is pentagonal, but minimizes the difference

from eulermath import pent, ispent

if __name__ == "__main__":
    minD = 9999999
    # For this range of pmax, the first solution is correct
    pmax = 10000
    for jj in range(1, pmax+1):
        for kk in range(jj, pmax+1):
            Pj = pent(jj)
            Pk = pent(kk)
            # make sure difference is positive
            Pd = Pk-Pj
            # print "difference: %d %d" % (Pd, ispent(Pd))
            if ispent(Pj+Pk) and ispent(Pd):
                print "found a pair that satisifieds. difference is %d" % (Pd)
                if Pd < minD:
                    minD = Pd
                    break

    print ("Searched up to the %dth pentagonal number, " +
           "minimum distance found was: %d" % (pmax, minD))
