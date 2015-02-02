from eulermath import coinage

# Ways of making change using a set list of coins

if __name__ == "__main__":
    coinlist = [1, 2, 5, 10, 20, 50, 100, 200]
    print "There are " + str(coinage(12, coinlist)) +
    " ways to make change for 12c, and"
    print str(coinage(200, coinlist)) +
    " ways to make change for 200c using euroinas."
