# Find the maximum digit sum of a^b, where a,b <= 100

from eulermath import int2array

if __name__ == "__main__":
    nmax = 100
    smax = 0
    for a in range(1, nmax+1):
        for b in range(1, nmax+1):
            p = a**b
            s = sum(int2array(p))
            # print "%d^%d = %d, digit sum = %d" % (a,b,p,s)
            if s > smax:
                smax = s
                # print "found a larger sum"
        print "%d/%d complete" % (a, nmax)

    print "The maximum digit sum is: %d" % (smax)
