"""
Example 1:

Input: arr = [100,200,150,1000]
 Output: 4
 Explanation: All four apples can be fitted in, because of their weight and 1450.
"""
def maxNumberOfApples(arr):
    cartSum = 0
    arr.sort()
    for i,wt in enumerate(arr):
        if(cartSum+wt>5000):
            return i
        cartSum+=wt
