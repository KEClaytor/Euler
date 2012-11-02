from eulermath import wordworth
from eulermath import tri

# Import the data
fnames = open('Euler42.dat')
for line in fnames:
    # Remove " and split by ,
    linenq = line.replace('"','')
    words = linenq.split(',')

ntriwords = 0
for word in words:
    n = 0
    wval = wordworth(word)
    # Keep increasing the triangle number until we either
    #  find it is a triangle number or tn > wordvalue (not a triangle word)
    while tri(n) <= wval:
        if tri(n) == wval:
            ntriwords += 1
            break
        n += 1
    #print word, wval, n, tri(n)  # Debugging

print "The list of words contains:", ntriwords, "triangle words."
