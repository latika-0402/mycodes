class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n=len(nums)
        result=[]
        d=collections.Counter(nums)
        for i,j in d.items():
            if j>n//3:
                result.append(i)
        return result