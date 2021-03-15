### Product except self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = 1
        n = len(nums)
        prod_arr = [1 for i in range(n)]
        ## Left multiplication
        for i in range(n):
            prod_arr[i] = temp
            temp *= nums[i]
        ## Right multiplication
        temp = 1
        for i in range(n-1,-1,-1):
            prod_arr[i] *= temp
            temp *= nums[i]
        return prod_arr       
