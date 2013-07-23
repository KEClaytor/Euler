# Find the next number after 40755 that is:
#  trangular, pentagonal, and hexagonal

from eulermath import tri, pent, hex, istri, ispent, ishex
## Testing - print out numbers and check them
#for i in range(40):
#    print "%d ist? %d isp? %d ish? %d" % (i,istri(i), ispent(i), ishex(i))

# Hexagonal numbers have the largest jumps in them, start with H(143) and go up
n = 143 # for testing set below 143 and see if it finds H(143)
found = False
while not found:
    n+=1
    Hn = hex(n)
    # There are fewer pentagonal numbers than triangular
    if ispent(Hn):
        if istri(Hn):
            found = True
            tn = istri(Hn)
            pn = ispent(Hn)

print "The next triangular, pengagonal, and hexagonal number is:"
print "\t\tT(%d) = T(%d) = H(%d) = %d" % (tn,pn,n,Hn)
