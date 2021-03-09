def solution(X, A):
    lookup = [0] * X
    for time in range(len(A)):
        pos = A[time]
        if(lookup[pos-1]==0):
            lookup[pos-1] = 1
            X -= 1
            if X==0:
                return time
    return -1
