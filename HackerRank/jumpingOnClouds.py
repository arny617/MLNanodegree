def jumpingOnClouds(c):
    i = 0
    jumps = 0
    l = len(c)
    while(i<l-1):
        if(l==i+2):
            i+=1
        elif(c[i+2]==0):
            i+=2
        else:
            i+=1
        jumps+=1
    return jumps
