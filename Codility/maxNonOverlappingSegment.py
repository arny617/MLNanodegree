## A: Array with start of each segment
## B: Array with end of each segment
## Sorted by end segment
def maxNonOverlappingSegment(A,B):
    prev_end = -1
    count = 0
    for i in range(len(A)):
        if A[i]>prev_end:
            count+=1
            prev_end = B[i]
    return count
    
