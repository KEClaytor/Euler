# Import the data
# Open the file -> read the lines
# Then for each line perform int on each element
fnames = open('Euler11.dat')
lines = fnames.readlines()
data = [map(int,line.strip().split()) for line in lines]
#print dataint

maxprod = 0
for row in range(0,17):
    for col in range(0,17):
        rval = data[row][col] * data[row][col+1] * data[row][col+2] * data[row][col+3]
        vval = data[row][col] * data[row+1][col] * data[row+2][col] * data[row+3][col]
        dval = data[row][col] * data[row+1][col+1] * data[row+2][col+2] * data[row+3][col+3]
        sval = data[row][col+3] * data[row+1][col+2] * data[row+2][col+1] * data[row+3][col]
        cmax = max([rval,vval,dval,sval])
        if cmax > maxprod:
            maxprod = cmax

print "The max product of 4 horizontal, vertical or diagonal values is:", maxprod
