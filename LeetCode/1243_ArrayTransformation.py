### Leetcode 1243: Array Transformation ##
def arrayTransform(arr):
    l = len(arr)
    arr_cpy = None
    while(arr!=arr_cpy):
        arr_cpy = arr[:]
        for i in range(1,l-1):
            flag = False
            if(arr_cpy[i]>arr_cpy[i-1] and arr_cpy[i]>arr_cpy[i+1]):
                arr[i]-=1
                flag = True
            elif(arr_cpy[i]<arr_cpy[i-1] and arr_cpy[i]<arr_cpy[i+1]):
                arr[i]+=1
                flag = True
    return arr
