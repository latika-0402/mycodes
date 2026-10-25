class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        nums.sort()
        result=[]
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                result.append(nums[i])
                i+=2
            else:i+=1
        return result
                
        