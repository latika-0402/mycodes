from collections import Counter
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        h=Counter(nums)
        for i,j in h.items():
            if j==1:
                return i
        
        