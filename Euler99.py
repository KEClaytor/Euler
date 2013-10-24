# Largest exponential
# Compare exponentials and see which is larger

from math import log

# Import the data
lline = 0
lbase = 1
lexp = 1
cline = 0
fname = open('Euler99.dat')
for line in fname:
    nline = line.strip('\n')
    row = nline.split(',')
    cline += 1
    base = int(row[0])
    exp = int(row[1])
    if (exp*log(base) > lexp*log(lbase) ):
        lline = cline
        lbase = base
        lexp = exp

print "The line with the largest exponential is: " + repr(lline)

