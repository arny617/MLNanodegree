def cyclicRotation(A,K):
    l = len(A)
    if(l==0):
        return A
    K = K%l
    if(K==0):
        return A
    return (A[-K:] + A[:l-K])
