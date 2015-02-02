# Find the number of unique ways we can write out
#  all 1-9 pandigital products, eg; 39*186=7254

from eulermath import makepandigital, array2int


# Splits up the pandigital number into it's components
#  And checks them for a valid product rule
def checksub(pan):
    prods = []
    for ii in range(1, 8):
        a = array2int(pan[0:ii])
        for jj in range(ii+1, 9):
            b = array2int(pan[ii:jj])
            c = array2int(pan[jj::])
            # print "%d" % (array2int(pan))
            # print "%d * %d =? %d -> %d" % (a,b,c,a*b==c)
            if (a*b == c):
                prods.append((a, b, c))
    return prods

if __name__ == "__main__":
    plist = makepandigital(9)
    prodlist = []
    prodsum = 0
    prodsumlist = []
    for pan in plist:
        prods = checksub(pan)
        if len(prods) > 0:
            print ""
            print "Found %d product combinations for the pandigital %d" %
            (len(prods), array2int(pan))
            # Check that each new element isn't already
            # in our list before we add it
            for prod in prods:
                no = (prod[0], prod[1], prod[2])
                ro = (prod[1], prod[0], prod[2])
                na = 0
                # if (no in prodlist):
                #     print repr(no) + " no already in"
                # if (ro in prodlist):
                #     print repr(ro) + " ro already in"
                if (no not in prodlist) and (ro not in prodlist):
                    # print "appending " + repr(no)
                    prodlist.append(no)
                    prodsum += no[2]
                    na += 1
                print "Appended %d of those" % (na)
                prodsumlist.append(prod[2])

    print prodlist
    print "There are %d unique 1-9 pandigital products." % (len(prodlist))
    print "The sum of their products is: %d" % (prodsum)
    print ("The sum of the unique products is: %d" %
           (sum(list(set(prodsumlist)))))
