### Climbing stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1: return 1

        ways1, ways2 = 1, 1

        for i in range(2, n + 1):
            ways = ways1 + ways2
            ways2 = ways1
            ways1 = ways

        return ways1
