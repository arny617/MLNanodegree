### Based on caterpillar approach
def countDistinctSlices(M,A):
    l = len(A)
    head = 0
    inSlice = [False]*(M+1)
    countSlice = 0
    for tail in range(l):
        while(head<l and not inSlice[A[head]]):
            inSlice[A[head]] = True
            countSlice += (head-tail)+1
            head += 1
            
            if countSlice>1000000000:
                return 1000000000
        inSlice[A[tail]] = False
    return countSlice
