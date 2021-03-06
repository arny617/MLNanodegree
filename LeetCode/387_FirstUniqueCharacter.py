### Find first unique character
class Solution:
    def firstUniqChar(self, s: str) -> int:
        S = 'abcdefghijklmnopqrstuvwxyz'
        indices = [s.index(c) for c in S if s.count(c) == 1]
        return min(indices) if indices else -1
