def maxSubsetSum(arr):
    inc = 0
    exc = 0
     
    for i in arr:   
        # Current max excluding i (No ternary in  
        # Python) 
        new_exc = exc if exc>inc else inc 
         
        # Current max including i 
        inc = exc + i 
        exc = new_exc 
      
    # return max of incl and excl 
    return (exc if exc>inc else inc)
