class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result=0
        nums.sort()
        for i in range(len(nums)):
            result=result^nums[i]
        return result
        