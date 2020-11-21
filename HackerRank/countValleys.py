def countingValleys(n, s):
    count=0
    prev = ""
    value = 0
    for char in s:
        if(char=='U'):
            value+=1
        elif(char=='D'):
            value-=1
        if(value==0 and char=='U'):
            count+=1
        prev=char
    return count
