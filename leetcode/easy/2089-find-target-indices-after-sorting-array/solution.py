class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        result=[]
        for i,nums in enumerate(nums):
            if nums==target:
                result.append(i)
        return result
        