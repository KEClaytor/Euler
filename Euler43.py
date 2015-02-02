# Find the sum of all 0-9 pandigital numbers
#  where the second to 4th digits are divisible by 2
#  the thrid to 5th divisible by 3, and so on (divisible by primes)

from eulermath import makepandigital


def substrdiv(string):
    subdiv = 1
    # Make the prime array list
    pl = [0, 1, 2, 3, 5, 7, 11, 13, 17]
    for si in range(2, 9):
        substr = string[si-1:si+2]
        div = pl[si]
        # print ("subgroup: " + substr + " % " +
        #        repr(div) + " = " + repr((int(substr)%div)))
        if (int(substr) % div != 0):
            subdiv = 0
            break
    return subdiv

if __name__ == "__main__":
    pandigital09 = makepandigital(9, False, 0)
    total = 0
    for num in pandigital09:
        # Make it into a string
        s09 = ''.join(str(x) for x in num)
        # make sure we don't have a leading zero
        if s09 != str(int(s09)):
            continue
        # Check the sub-string divisibliilty
        if substrdiv(s09):
            total += int(s09)

    print ("The total of 0-9 pandigital numbers with this property is: "
           + repr(total))
