import itertools

intstr = '123456789'
permlist = itertools.permutations(intstr,9)
for x in permlist:
    print x

