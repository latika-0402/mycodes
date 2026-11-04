class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        d=collections.Counter(nums)
        for i,j in d.items():
            if j>=2:
                return i
                break