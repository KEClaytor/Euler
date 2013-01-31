# A linear algebra package
# Kevin Claytor
# 2012-11-30

def dot(va,vb):
    # Error checking va and vb need to be the same length
    if len(va) == len(vb):
        for ii in range(0,len(va)):
            dotprod = va[ii] * vb[ii]

    pass

def norm(va):
    return sqrt(sum(va**2))

# Return a normalized vector
def normalize(va):
    return va/norm(va)
