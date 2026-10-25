class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        max_val=max(nums)
        return nums.index(max_val)
        