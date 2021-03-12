### Max Counters
def maxCounter(N,A):
    maxVal = 0
    counterArray = [0]*N
    startLine = 0
    for i in A:
        if(i>N):
            startLine = maxVal
        elif(counterArray[i-1]<startLine):
            counterArray[i-1] = startLine + 1
        else:
            counterArray[i-1] += 1
        if(i<=N and counterArray[i-1]>maxVal):
            maxVal = counterArray[i-1]
    for i in range(N):
        if counterArray[i]<startLine:
            counterArray[i] = startLine
            
    return counterArray
