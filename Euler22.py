def nameworth(name):
    worth = 0
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for letter in name:
        # Add the index to the name value, account for the zero offset
        worth += alphabet.index(letter) + 1
    return worth

# Import the data
fnames = open('Euler22.dat')
i = 1
for line in fnames:
    # Remove " and split by ,
    linenq = line.replace('"','')
    names = linenq.split(',')

# Sort the list
names.sort()

totalnamescore = 0
for index in xrange(0,len(names)):
    namescore = nameworth(names[index]) *(index+1)
    #print names[index], nameworth(names[index]), namescore
    totalnamescore += namescore

print "The total name score of the file is:", totalnamescore
