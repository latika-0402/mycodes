class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        result=0
        i=0
        while i<len(nums):
            if nums[i] < minK or nums[i] > maxK:
                i += 1
                continue
            start = i
            while i < len(nums) and minK <= nums[i] <= maxK:
                i += 1
            l=i-start
            result+=l*(l+1)//2
        return result
            
        
        