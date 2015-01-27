# Euler24:
# Find the 1 millionth lexographic permutation of {0,1,2,3,4,5,6,7,8,9}\
from math import factorial
from eulermath import array2int

# Let's use some math first
# Overally there will be 10 options for our 1st element, then 9 for the 2nd...
# Giving a total (10)*(9)*(8)*(7)*... = 10! = 3628800 permutations
#
# Now we know we're going to go in lexographic order, so if we set
# 0 as the first element, then we have 9! = 362880 options for the others
# This is < 1M, so let's add this value to 1*{0,2,3,...,9} = 9!
#
# Now we have 725760 permutations with 0 and 1 in the first slot, adding in
# the possible permutations with 2 in the first slot gives 1088640
# So now we know that we have to start with 2.
#
# Now we can see how the algorithm will work, fix one, start increasing the
# others until we exceed 1M (if we are equal to 1M then it's exactly the last
# in that permutation cycle)

if __name__ == "__main__":
    # for lt in [1,2,3,4,5,6]:
    for lt in [1000000]:
        # Test case
        # nums = [0, 1, 2]
        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        nleft = len(nums)
        # lt = 2
        # the millionth lexographic term, it will be constructed as we go
        mlt = []
        cvalue = 0

        while nleft > 1:
            # print ""
            naddperms = factorial(nleft-1)
            # print "List: " + repr(nums)
            # print "Current sum: " + repr(cvalue)
            # print "Additional terms: " + repr(naddperms)
            # print "Target term: " + repr(lt)
            num = 0
            while num <= nleft:
                # print repr(num) + "  " + repr(nums[num-1]) +
                # "  " + repr(cvalue + (num)*naddperms)
                if cvalue + (num)*naddperms == lt:
                    nt = nums.pop(num-1)
                    mlt.append(nt)
                    nums.reverse()
                    mlt.extend(nums)
                    nums = []
                    nleft = 0
                    break
                elif cvalue + (num)*naddperms > lt:
                    cvalue += (num-1)*naddperms
                    nt = nums.pop(num-1)
                    mlt.append(nt)
                    break
                elif num == nleft:
                    nt = nums.pop(num)
                    mlt.append(nt)
                    break
                num += 1
            # print mlt
            nleft = len(nums)
        print repr(array2int(mlt)) + " is the " + repr(lt) +
        "th lexographic permutation of the set"
