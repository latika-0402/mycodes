class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        last = -1
        ans = 0
        
        for i, num in enumerate(nums):
            if minK <= num <= maxK:
                ans += i - last
            else:
                last = i
                
        return ans
        
        