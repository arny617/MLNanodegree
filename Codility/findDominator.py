def findDominator(A):
    count = 0
    dItem = None
    for i in range(len(A)):
        if count==0:
            dItem = A[i]
            count+=1
        elif(A[i] != dItem):
            count-=1
        elif(A[i] == dItem):
            count+=1
    if(A.count(dItem)>len(A)/2):
        return A.index(dItem)
    else:
        return -1
