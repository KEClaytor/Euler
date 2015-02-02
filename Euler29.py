
if __name__ == "__main__":
    # nmax = 5 # Test case, should give 15 distinct terms
    nmax = 100
    mylist = []
    for a in range(2, nmax+1):
        for b in range(2, nmax+1):
            mylist.append(a**b)

    # Remove the duplicates
    mylist = list(set(mylist))
    # And count
    print "There are:", len(mylist), "unique elements in the list."
