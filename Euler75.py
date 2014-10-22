# Find the number of integer right triangles with
#  side length < 1.5M and only one right triangle combination
from eulermath import coprime, arraymult

# This is a generator for the primitive Pythagorean triples
def generate_primitive_triple():
    m = 2
    n = 1
    while True:
        # Generates a primitive triple if:
        #   m and n are coprime
        #   and m-n is odd
        if coprime(m,n) and ((m-n)%2 != 0):
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            yield sorted([a, b, c])
        n += 1
        if m <= n:
            m += 1
            n = 1

if __name__ == "__main__":
    ppt = generate_primitive_triple()
    max_L = 1500000
    num_triples = [0]*(max_L+1)
    triple = ppt.next()
    base_triple_sum = sum(triple)
    #while base_triple_sum <= max:
    while base_triple_sum < max_L:
        #print "Current triple: " + repr(triple)
        n = 1
        triple_sum = base_triple_sum
        while triple_sum <= max_L:
            #print "    Has lengths: " + repr(triple_sum)
            num_triples[triple_sum] += 1
            n += 1
            triple_sum = base_triple_sum*n
        triple = ppt.next()
        base_triple_sum = sum(triple)
    print "We can form only one integer right triangle for %d lengths of wire < %d" % (num_triples.count(1), max_L)
