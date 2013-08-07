# Chain: Add the square of the digits to form a new number
# Chains terminate in either 1 or 89!
# How many starting values below 1M terminate in 89
from eulermath import int2array

def next(val):
    return sum([x**2 for x in int2array(val)])

term_01 = []
term_89 = []
max = 10**7
for s in range(1,max):
    nt = s
    chain = [s]
    while (nt != 89) and (nt != 1):
        nt = next(nt)
        chain.append(nt)
    #print repr(chain)
    if nt == 89:
        term_89.append(s)
    else:
        term_01.append(s)
    #if s%(max/10) == 0:
    #    print "+10%"

#print "One terminal chains: " + repr(term_01)
#print "89 terminal chains: " + repr(term_89)
print "%d starting numbers below %d have chains that arrive at 89." % (len(term_89),max)
