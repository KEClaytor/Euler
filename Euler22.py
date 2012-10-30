from eulermath import wordworth

# Import the data
fnames = open('Euler22.dat')
for line in fnames:
    # Remove " and split by ,
    linenq = line.replace('"','')
    names = linenq.split(',')

# Sort the list
names.sort()

totalnamescore = 0
for index in xrange(0,len(names)):
    namescore = wordworth(names[index]) *(index+1)
    #print names[index], nameworth(names[index]), namescore
    totalnamescore += namescore

print "The total name score of the file is:", totalnamescore
