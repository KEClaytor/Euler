# Cubic permutations
# Find the smallest cube where five permutations
#  of it's digits are also cubes

from eulermath import array2int, int2array, nintdigits, ispermutation

def find_perm_pairs(arr):
    nelem = len(arr)
    perms = []
    for ii in range(nelem):
        cperm = []
        for jj in range(ii, nelem):
            if ispermutation(arr[ii], arr[jj]):
                cperm.append(arr[jj])
        perms.append(cperm)
    return perms

if __name__ == "__main__":
    # Test case, should come up with longest combo: 3
    #                   min cube for combo: 345
    #mylist = range(1,1000)
    mylist = range(1, 10000)
    cubes = map(lambda(x): x**3, mylist)
    # Now see if the cubes are permutations of each other
    combos = find_perm_pairs(cubes)
    combo_lengths = map(len, combos)
    max_combo_length = max(combo_lengths)
    min_cube_for_combo = combo_lengths.index(max_combo_length)
    print "max combo length: %d, min cube for combo: %d" % \
        (max_combo_length, min_cube_for_combo+1)
