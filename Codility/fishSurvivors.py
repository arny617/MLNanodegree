def fishSurvivors(A,B):
    survivors = 0
    stack = []
    for i in range(len(A)):
        weight = A[i]
        if(B[i]==1):
            stack.append(weight)
        else:
            weightDown = stack.pop() if stack else -1
            while(weightDown!=-1 and weightDown<weight):
                weightDown = stack.pop() if stack else -1
            if weightDown==-1:
                survivors += 1
            else:
                stack.append(weightDown)
    return survivors + len(stack)
