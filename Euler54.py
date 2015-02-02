# Analyze a file of poker hands and find out how many p1 wins

import re


# Split tha hand into a more amiable form
def expandhand(hand):
    vals = []
    suits = []
    valdict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
               '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    for card in hand:
        vals.append(valdict[card[0]])
        suits.append(card[1])
    return (vals, suits)


# Count how many of each suit is in the hand
def countsuit(suit):
    gs = ['C', 'D', 'H', 'S']
    return [suit.count(x) for x in gs]


# And how many of each card number is in each hand
def countvals(vals):
    return [vals.count(x) for x in range(15)]


# Determines if a set is a straight
def is_straight(ncard):
    iss = False
    if max(ncard) == 1:
        xi = ncard.index(1)
        if min(ncard[xi:xi+5]) == 1:
            iss = True
    return iss


# And if it is a flush
def is_flush(nsuit):
    isf = False
    if max(nsuit) == 5:
        isf = True
    return isf


# Routines to determine if the hand is a poker hand
def is_royalflush(nsuit, ncard, highcard):
    if is_flush(nsuit):
        if is_straight(ncard):
            if highcard == 14:
                return True
    return False


def is_straightflush(nsuit, ncard):
    if is_flush(nsuit):
        if is_straight(ncard):
            return True
    return False


def is_fourofakind(ncard):
    if max(ncard) == 4:
        return True
    return False


def is_fullhouse(ncard):
    if (ncard.count(3)) and (ncard.count(2)):
        return True
    return False


def is_threeofakind(ncard):
    if ncard.count(3):
        return True
    return False


def is_twopair(ncard):
    if ncard.count(2) == 2:
        return True
    return False


def is_pair(ncard):
    if ncard.count(2):
        return True
    return False


# Subroutine for determining the value of a hand
# Returns a type value:
#  royal flush = 9 (high)
#  high card = 0 (low)
# and a highcard value to split ties
def pokerhandvalue(hand):
    handval = 0
    cardval = 0
    (vals, suit) = expandhand(hand)
    nsuit = countsuit(suit)
    ncard = countvals(vals)
    # Start sorting
    highcard = max(vals)
    maxncard = ncard.index(max(ncard))
    if is_royalflush(nsuit, ncard, highcard):
        # print "Royal Flush"
        handval = 9
        cardval = 14
    elif is_straightflush(nsuit, ncard):
        # print "Straight Flush"
        handval = 8
        cardval = highcard
    elif is_fourofakind(ncard):
        # print "Four of a kind"
        handval = 7
        cardval = maxncard
    elif is_fullhouse(ncard):
        # print "Full House"
        handval = 6
        cardval = maxncard
    elif is_flush(nsuit):
        # print "Flush"
        handval = 5
        cardval = maxncard
    elif is_straight(ncard):
        # print "Straight"
        handval = 4
        cardval = highcard
    elif is_threeofakind(ncard):
        # print "Three of a kind"
        handval = 3
        cardval = maxncard
    elif is_twopair(ncard):
        # Two pair, make sure we get the higher of the two
        # print "Two pair"
        maxncard2 = ncard.index(max(ncard), maxncard+1)
        handval = 2
        cardval = max([maxncard, maxncard2])
    elif is_pair(ncard):
        # print "Pair"
        handval = 1
        cardval = maxncard
    else:
        # print "Highcard"
        handval = 0
        cardval = highcard
    return (handval, cardval)


def whowins(p1hand, p2hand):
    winner = 0
    (h1, c1) = pokerhandvalue(p1hand)
    (h2, c2) = pokerhandvalue(p2hand)
    if h1 > h2:
        winner = 1
    elif (h1 == h2):
        if c1 > c2:
            winner = 1
        elif c2 > c1:
            winner = 2
    else:
        winner = 2
    return winner

if __name__ == "__main__":
    fhands = open('Euler54.dat')
    p1wins = 0
    ngames = 0
    for hand in fhands:
        allcards = re.findall(r'[\d\S]\S', hand)
        p1 = allcards[0:5]
        p2 = allcards[5:10]
        winner = whowins(p1, p2)
        if winner == 1:
            p1wins += 1
        # print p1
        # print pokerhandvalue(p1)
        # print p2
        # print pokerhandvalue(p2)
        # print winner
        ngames += 1

    print "Player 1 wins %d of %d hands." % (p1wins, ngames)
