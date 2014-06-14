# Find the only set of 6-digit figurate (polygonal) numbers
# That is cyclic

from eulermath import gen_tri, gen_sqr, gen_pent, gen_hex, gen_hept, gen_oct
from eulermath import depth

def cyclic(cycle, search_lists):
    # See if there are other lists to search through
    #print len(search_lists)
    #print cycle
    if search_lists:
        test = str(cycle[0])[2:]
        #print test
        for ii in range(len(search_lists)):
            for next_elem in search_lists[ii]:
                if str(next_elem)[0:2] == test:
                    #print next_elem
                    # Pass on this element
                    # Make note to take a copy of the list
                    #  and pop this list from that
                    remaining_lists = search_lists[:]
                    remaining_lists.pop(ii)
                    next_cycle = cyclic([next_elem], remaining_lists)
                    cycle.append(next_cycle)
        return cycle

    else:
        # No more lists to iterate over
        return cycle

def extract6cycle(cycles, current_cycle, current_depth, input_list):
    this_elem = input_list[0]
    this_cycle = current_cycle + [this_elem]
    this_depth = current_depth + 1;
    # If we can continue travelling down the list do so
    if len(input_list) > 1:
        remaining_lists = input_list[1:]
        for test_list in remaining_lists:
            cycles = extract6cycle(cycles, this_cycle, this_depth, test_list)
    else:
        cycles.append(this_cycle)
    return cycles

def checkcycle(cycle):
    a = str(cycle[0])
    b = str(cycle[-1])
    if a[0:2] == b[2:]:
        return True
    else:
        return False

if __name__=="__main__":
    # Get the list of the figurate numbers
    # Use a generator for each of them
    generators = [gen_tri(), gen_sqr(), gen_pent(), gen_hex(), gen_hept(), gen_oct()]
    figurates = [[] for i in range(len(generators))]
    # Generate strings of all the 6-digit figurate numbers
    for ii in range(len(generators)):
        for figurate in generators[ii]:
            sfig = str(figurate)
            if len(sfig) < 4:
                continue
            elif len(sfig) == 4:
                figurates[ii].append(figurate)
            else:
                break
    # Sort by the number of elements
    #print figurates
    figurates = sorted(figurates, key=lambda x: len(x))
    #print map(len, figurates)

    possible_cycles = []
    for fig in figurates[0]:
        cycle = cyclic([fig], figurates[1:])
        if depth(cycle) >= 6:
            possible_cycles.append(cycle)

    # Convert to int and flatten out
    for testlist in possible_cycles:
        for flat in extract6cycle([],[],0,testlist):
            if len(flat) == 6 and checkcycle(flat):
                print "Found it!:"
                print flat
                print sum(flat)
