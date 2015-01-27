import math


# Subfunction to write a number as a word
def num2word(n):
    waones = ["", "one", "two", "three", "four",
              "five", "six", "seven", "eight", "nine"]
    watens = ["", "ten", "twenty", "thirty", "forty",
              "fifty", "sixty", "seventy", "eighty", "ninety"]
    watwns = ["", "eleven", "twelve", "thirteen", "fourteen",
              "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    wordstr = ""
    andflag = 0
    if (n >= 1000):
        thous = int(math.floor(n/1000))
        wordstr += waones[thous] + "thousand"
        n -= thous*1000  # Update n
        andflag = 1
    if (n >= 100):
        hunds = int(math.floor(n/100))
        wordstr += waones[hunds] + "hundred"
        n -= hunds*100
        andflag = 1
    # Handle the special case 11-19
    if (n > 10) & (n < 20):
        if andflag == 1:
            wordstr += "and"
        ones = n % 10
        wordstr += watwns[ones]
    elif (n > 0):
        # Do the tens place
        if andflag == 1:
            wordstr += "and"
        if (n >= 10):
            tens = int(math.floor(n/10))
            wordstr += watens[tens]
            n -= tens*10
            # and the ones place
        if (n > 0):
            wordstr += waones[n]
    return wordstr

if __name__ == "__main__":
    # n = input("Number to convert to string: ")
    # print num2word(n)
    lower = 1
    # upper = 5 # test case, should give 19
    upper = 1000
    total = 0
    for x in range(lower, upper+1):
        # print x, num2word(x), len(num2word(x))
        total += len(num2word(x))

    print "The number of letters in the numbers",
    lower, "to", upper, "is:", total
