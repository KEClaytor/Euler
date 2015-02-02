# Double base palindromes, find binary palindromes and decimal palindromes
# Sum them up all of them < 1M
from eulermath import ispalindrome


def make_palindrome_half(n):
    superlist = []
    if n > 0:
        sublist = make_palindrome_half(n-1)
        for item in sublist:
            superlist.append(item + '1')
            superlist.append(item + '0')
    else:
        superlist = ['1', '0']
    return superlist


def str_bin2int(sb):
    myval = 0
    for ind in range(len(sb)):
        myval += int(sb[ind])*2**ind
    return myval

if __name__ == "__main__":
    # Search through binary palindromes, as they should be easier to make
    # 1M requires at least 20 binary digits
    binary_len = 20
    plisthalf = make_palindrome_half(binary_len/2)
    plistfull = []
    for phalf in plisthalf:
        # Take our half palindrome and make it a full palindrome
        temp_pal_even = phalf+phalf[::-1]
        # Don't forget the odd length palindromes
        temp_pal_odd = phalf+phalf[:-1][::-1]
        # strip leading and trailing zeros
        plistfull.append(temp_pal_even.rstrip('0').lstrip('0'))
        plistfull.append(temp_pal_odd.rstrip('0').lstrip('0'))

    # Trim off the last two values, since they're empty
    #  (side effect of including the odds above)
    plistfull = plistfull[1:-2]

    palsum = 0
    for palindrome in plistfull:
        intval = str_bin2int(palindrome)
        print (repr(palindrome) + ' ' + repr(intval) + ' ' +
               repr(ispalindrome(intval)))
        if intval < 10**6:
            if ispalindrome(intval):
                palsum += intval
    print 'Value of double-base palindromes < 1M = ' + repr(palsum)
