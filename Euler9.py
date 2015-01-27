# Find possible pythorgean tripples using euler's method
# I figure that's appropriate
# the extra form of k convers all primes, but may repeat
# I'm using it as a function purely to break out of the multiple loops

if __name__ == "__main__":
    for m in range(1, 500):
        for n in range(1, m):
            for k in range(1, 50):
                a = k*(m**2 - n**2)
                b = k*(2*m*n)
                c = k*(m**2 + n**2)
                if (a+b+c == 1000):
                    print "[", a, ",", b, ",", c, "]"
                    print c**2 - a**2 - b**2
                    print a+b+c
                    print "Found! The product is:", a*b*c
