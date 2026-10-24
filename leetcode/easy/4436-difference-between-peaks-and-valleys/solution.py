class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        peakval=[]
        valval=[]
        for i in range(1,len(nums)-1):
            if nums[i]> nums[i-1] and nums[i]>nums[i+1]:
                peakval.append(nums[i])
            elif nums[i]<nums[i-1] and nums[i]<nums[i+1]:
                valval.append(nums[i])
        return (sum(peakval)-sum(valval))
        