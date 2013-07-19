# Find the # of non-distinct nCr's > 1M for 1 <= n <= 100

from eulermath import nCr

# We know that the first > 1M nCr is 23^C_10
# We also know that if nCr > 1M then nC(r+1) > 1M IF
#  r+1 < n-p where p is min(m) where nCm > 1M

numways = 0
for n in range(23,101):
    for r in range(1,n):
        if nCr(n,r) >= 1000000:
            numways += n+1 - 2*r
            continue

print numways
