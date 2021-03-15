### Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0 = nums.count(0)
        nums[:] = (value for value in nums if value != 0)
        for i in range(count0):
            nums.append(0)
