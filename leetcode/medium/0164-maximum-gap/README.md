# Maximum Gap

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums`, return  *the maximum difference between two successive elements in its sorted form*. If the array contains less than two elements, return `0`.

You must write an algorithm that runs in linear time and uses linear extra space.

 

 **Example 1:** 

```
Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.

```

 **Example 2:** 

```
Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.

```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- 0 <= nums[i] <= 109

## Solution

**Language:** Python  
**Runtime:** 147 ms (beats 64.79%)  
**Memory:** 31.9 MB (beats 72.12%)  
**Submitted:** 2026-10-25T16:30:07.656Z  

```py
class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums)<2:
            return 0
        nums.sort()
        max_gap=0
        for i in range(1,len(nums)):
            current=nums[i]-nums[i-1]
            max_gap=max(max_gap,current)
        return max_gap
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-gap/)