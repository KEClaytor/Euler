n = input("Max bound?: ")
total = 0
#list = []
for ii in range(1,n):
    if (ii % 3 == 0) | (ii % 5 == 0):
        total += ii
        #list.append(ii)

print "Sum of multiples of 3 or 5 up to (not including)", n, "is:", total
#print "The multiples of 3 or 5 below ", n, " is: ", list
