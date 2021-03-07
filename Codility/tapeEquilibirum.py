def tapeEquilibirium(A):
    left = A[0]
    right = sum(A[1:])
    minD = abs(left-right)
    for i in range(1,len(A)-1):
        left += A[i]
        right -= A[i]
        if(minD>abs(left-right)):
            minD = abs(left-right)
    return minD
