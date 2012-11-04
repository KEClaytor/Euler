from eulermath import roman2int
from eulermath import int2roman
#print "VII", roman2int("VII"), "=7"
#print "MCLIV", roman2int("MCLIV"), "=1154"

# Import the data
froman = open('Euler89.dat')

total = 0
ncharorig = 0
ncharnew = 0
for line in froman:
    rnum = line.rstrip('\n')
    rnew = int2roman(roman2int(rnum))
    print rnum, roman2int(rnum), rnew
    ncharorig += len(rnum)
    ncharnew += len(rnew)
    total += roman2int(rnum)
    

#for x in range(3000,5000):
    #print x, int2roman(x)
print "The total value of the roman numerals in the file is:", total
print "They were originally written with", ncharorig, "characters"
print " but in their minimal form only require", ncharnew, "characters"
print " allowing one to save", ncharorig -ncharnew, "characters."
