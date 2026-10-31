class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        d=collections.Counter(nums)
        for i,j in d.items():
            if j>len(nums)//2:
                return i
        