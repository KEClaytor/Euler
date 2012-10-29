from eulermath import nCr
# Check that our nCr is working correctly
# by printing out the first few layers of pascal's triangle

for n in range(1,5):
    opts = ''
    row = []
    for r in range(1,n):
        opts += ' ('+(n)+','+r+')'
        row.append(nCr(n,r))
    print row
