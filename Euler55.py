from eulermath import ispalindrome
from eulermath import intreverse


def islychrel(n):
    isl = 1
    iter = 0
    while iter < 50:
        nprn = n + intreverse(n)
        # A lychrel numner is one that does NOT form
        #  a palindrome through reverse and add
        if ispalindrome(nprn) == 1:
            isl = 0
            break
        else:
            n = nprn
        iter += 1
    return isl

# print "Int reversing"
# print 123, intreverse(123)
# print "Palindromes"
# print 1234, ispalindrome(1234)
# print 4224, ispalindrome(4224)

# print "Lychrel-ness"
# print 47, islychrel(47)
# print 349, islychrel(349)
# print 196, islychrel(196)

if __name__ == "__main__":
    nlych = 0
    nmax = 10000
    n = 1
    while n < nmax:
        if islychrel(n):
            nlych += 1
        n += 1

    print "The number of Lychrel numbers below:", nmax, "is:", nlych
