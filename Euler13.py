# TODO: replace with the eulermath function

def str2intarray(strin):
    array = [int(i) for i in strin]
    return array

# Import the data from our file of numbers
# Keep only the last 10 digits of each number
# since we're only interested in finding the
# last ten digits of the sum
sum = 0
file = open("Euler13.dat")
for line in file:
    sum += int(line[0:14])

print sum
