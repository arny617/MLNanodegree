def minAbs2SumArray(A):
    l = len(A)
    A.sort()
    start = 0
    end = l-1
    m = 2000000000
    while(start<end):
        m = min(abs(A[start]+A[end]),m)
        if abs(A[start])>abs(A[end]):
            start+=1
        else:
            end-=1
    return m
