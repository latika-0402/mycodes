class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i,j in enumerate(nums):
           s=sum(int(digit) for digit in str(j))
           if s==i:return i
        return -1
                
        