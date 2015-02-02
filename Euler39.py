# Which value of p <= 1000 maximizes the number of
#  integer right triangles with perimeter p

from math import sqrt


# Returns possible integer right triangles with perimeter p
# Uses that for a right triangle of sides a, b, c
#  a^2 + b^2 = c^2
#  a + b + c = p
# With a bit of algebra, we obtain
# b = (2*p*a - p^2) / (2*(a-p))
# We hit a maximum a when a = b, which occurs when;
# a <= (1 +- 1/sqrt(2))*p
# Since a < p we take the negative
def get_triangle_pairs(p):
    rtpairs = []
    amax = int((1-.707)*p)
    # print "amax = %d" % (amax)
    for a in range(1, amax+1):
        b = (2.0*p*a-p**2)/(2*a-2*p)
        # print "a=%d b=%d" % (a,b)
        if b == int(b):
            b = int(b)
            c = int(sqrt(a**2 + b**2))
            rtpairs.append((a, b, c))
    return rtpairs

# Test case, should return [(20,48,52),(24,45,51),(30,40,50)]
# print get_triangle_pairs(120)

if __name__ == "__main__":
    smax = 0
    pmax = 0
    for p in range(1, 1001):
        rtp = get_triangle_pairs(p)
        if len(rtp) > smax:
            smax = len(rtp)
            pmax = p

    print "A perimeter of %d produces %d right triangles." % (pmax, smax)
