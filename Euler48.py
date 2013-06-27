# Find the last 10 digits of the sequence:
#  1^1 + 2^2 +3^3 + ... + 1000^1000
# Check is:
#  1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317


max = 1000
total = 0
for x in range(1,max+1):
    num = str(x**x)
    total += int(num[-10::])

# Just print the last 10 digits
totalstr = str(total)
print totalstr[-10::]
