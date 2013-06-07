# Maximum path sum
# Start at the 2nd to bottom row
#  Update teh row value with the maximum of
#  the two possible elements below it
# Keep traversing upwards until the top is reached
# That is now the maximum path
# Example;
#   3
#  7 4
# 2 4 6
#8 5 9 3
#
#     3
#   7  4
# 10 13 15
#
#     3
#   20 19
#
#    23

# Import the data
mylist = []
fname = open('Euler67.dat')
for line in fname:
    nline = line.strip('\n')
    row = nline.split(' ')
    mylist.append( [int(x) for x in row] )

mylist.reverse()
for ii in range(1,len(mylist)):
    prow = mylist[ii-1]
    row = mylist[ii]
    for jj in range(len(row)):
        row[jj] = max([row[jj]+prow[jj],row[jj]+prow[jj+1]])
    mylist[ii] = row

print mylist[-1]

