def countTriangles(A):
    l = len(A)
    A.sort()
    count = 0
    for i in range(l-1,0,-1):
        l = 0
        r = i-1
        while(l<r):
            if(A[l]>A[i]-A[r]):
                count += r-l
                r-=1
            else:
                l+=1
    return count
