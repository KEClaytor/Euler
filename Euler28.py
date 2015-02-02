
# Specifies the length of a side
# nside = 5 # Test case, should give 101
nside = 1001

spiralsum = 1
n = 1
spacing = 2
diag = [1]

while (spacing < nside):
    for ii in range(0, 4):
        n += spacing
        spiralsum += n
        diag.append(n)
    spacing += 2

# print "Numbers on the diagonal", diag,
# "Which is a list of", len(diag), "elements"
print "Sum of the diagonal elements is", spiralsum
