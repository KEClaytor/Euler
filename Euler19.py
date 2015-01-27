# Compute # of sundays in 20th century
# KEC 1-31-2013


def isLeapYear(year):
    ly = False
    if year % 4 == 0:
        # Centuries have special cases
        if year % 100 == 0:
            if year % 400 == 0:
                ly = True
        else:
            ly = True
    return ly

if __name__ = "__main__":
    # Days in month vector
    daysinmonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    year = 1900
    month = 1
    sunday = 7  # The first sunday is Jan 7th 1900
    # Determine if we are a leapyear and set the daysinmonth accordingly
    if isLeapYear(year):
        daysinmonth[1] = 29
    else:
        daysinmonth[1] = 28

    # Account for the two sundays that fall on the first of the month
    # in 1900 - we are just computing those between:
    # Jan 1st, 1901 and Dec 31, 2000
    nfirstsundays = -2

    while year < 2001:
        # Now that we have updated to the next sunday...
        # see if this is the first of a month
        # print "sunday # = " + str(sunday) + " Month = " + str(month) +
        # " Year = " + str(year) + " nfirstsunday = " + str(nfirstsundays)
        if sunday == 1:
            nfirstsundays += 1
            # print "GOT ONE!"
        # increment by a week
        sunday = sunday + 7
        # See if that puts us in the next month
        if sunday > daysinmonth[month-1]:
            sunday = sunday % daysinmonth[month-1]
            month += 1
            # See if that puts us in the next year
            if month > 12:
                year += 1
                month = 1
                # Set days in month based on leap-year-age
                if isLeapYear(year):
                    daysinmonth[1] = 29
                else:
                    daysinmonth[1] = 28

    print "There are " + str(nfirstsundays) +
    " sundays that fall in on the first of the month in the 20th century."
