# Decoding a text file (cipher1.txt) using xor notation.
# Knowns: The key is three lower case ASCII letters
# While we'll likely be using UNICODE behind the scenes,
#  it overlaps with ASCII for the common (a-z,A-Z,0-9) chars
#  ord() -> takes us to the int value
#  chr() -> takes us to the string

# Letter frequency (high to low) is:
# etaoinshrdlcumwfgypbvkjxqz
# Question: Do we need the space key? (before e)

from operator import itemgetter
from time import sleep
import itertools
import string
import math


# From itertools, but I don't have >v2.7 when this was introduced
def combinations_with_replacement(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indices in itertools.product(range(n), repeat=r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)


# Takes a string to an ASCII list
def S2A(mystring):
    return map(ord, mystring)


# Takes an ASCII list to a string
def A2S(mylist):
    return ''.join([chr(ii) for ii in mylist])


# Takes in a string or list of ASCII values
#  and does XOR with a key string / list
def xortext(mytext, key):
    if isinstance(mytext, str):
        mytext = S2A(mytext)
    if not isinstance(key, str):
        key = A2S(key)
    # If the key is shorter repeat it
    if len(key) < len(mytext):
        keyrep = key*int((len(mytext)/len(key)+1))
    keyrep = S2A(keyrep)
    if isinstance(mytext, str):
        print "mytext is str"
    if isinstance(keyrep, str):
        print "keyrep is str"
    # Now do the xor operation
    xorstring = ''.join([chr(x ^ y) for x, y in zip(mytext, keyrep)])
    return xorstring


# Hisograms a list and returns a tuple of [(value), (frequency)]
# sorted by frequency
def hist(mylist):
    ulist = list(set(mylist))
    histtup = zip(ulist, [mylist.count(x) for x in ulist])
    return sorted(histtup, key=itemgetter(1), reverse=True)


def testxor():
    # Testing xor
    print repr(65 ^ 42)
    # Testing string <--> ASCII
    print plaintext
    apt = S2A(plaintext)
    print apt
    rpt = A2S(apt)
    print rpt

    plaintext = 'this is a test string'
    key = 'xyz'
    ciphertext = xortext(plaintext, key)
    decodetext = xortext(ciphertext, key)
    print plaintext
    print key
    print ciphertext
    print decodetext

if __name__ == "__main__":
    # Import the data - there is only one line
    fnames = open('cipher1.txt')
    for line in fnames:
        nline = line.strip('\n')
        chars = nline.split(',')

    message = map(int, chars)
    # print message

    # Import a list of common english words
    fwords = open('commonwords2.txt')
    commonwords = [line.strip('\n') for line in fwords]

    toplet = [' ', '.', ',', 'e', 't', 'a', 'o', 'i', 'n',
              's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w',
              'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x',
              'q', 'z']
    toplet.reverse()

    # Come up with a key based on
    #  1) the frequency of characters in the message
    #  2) and the most frequently used english letters
    #  3) the knowledge that the key is lowercase english letters
    freqchar = [elem[0] for elem in hist(message)]
    lowercase = string.ascii_lowercase
    poskey = []
    # print hist(chars)
    # print toplet[-6::]
    for ii in range(4):
        res = [chr(freqchar[ii] ^ ord(x)) for x in lowercase]
        print res
        for let in toplet[-6::]:
            if let in res:
                poskey.append(lowercase[res.index(let)])
        print poskey

    # We know the key is ascii lowercase, and 3 characters long
    # Permute over all of those and see if we get english back
    # Brute force solution
    print "Decrypting and looking for words with possible key values..."
    keylist = []
    nwordlist = []
    for fullcomb in combinations_with_replacement(poskey, 3):
        for comb in itertools.permutations(fullcomb):
            key = ''.join(x for x in comb)
            # print key
            recoveredtext = xortext(message, key)
            # Only search for words if all characters are < ASCII value 127
            if (max(S2A(recoveredtext)) < 128) and
            (min(S2A(recoveredtext)) > 31):
                # Search for the common words
                nwords = 0
                for word in commonwords:
                    if len(word) > 2:
                        if string.find(recoveredtext, word) != -1:
                            nwords += 1
            keylist.append(key)
            nwordlist.append(nwords)

    comblist = sorted(zip(keylist, nwordlist), key=itemgetter(1), reverse=True)
    bestguess = comblist[0]
    recoveredtext = xortext(message, bestguess[0])

    print "Decrypted message:"
    print recoveredtext

    print "Sum of ASCII values of message:" + repr(sum(S2A(recoveredtext)))
