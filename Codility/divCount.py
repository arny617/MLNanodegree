### a= Start of sequence, b=end of sequence, k=divisor
def divCount(a,b,k):
    from math import ceil, floor
    return floor(b/k)-ceil(a/k)+1
