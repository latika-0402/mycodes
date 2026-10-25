# Find All Duplicates in an Array

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums` of length `n` where all the integers of `nums` are in the range `[1, n]` and each integer appears  **at most**   **twice**, return  *an array of all the integers that appears  **twice***.

You must write an algorithm that runs in `O(n)` time and uses only  *constant*  auxiliary space, excluding the space needed to store the output

 

 **Example 1:** 

```
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

```

 **Example 2:** 

```
Input: nums = [1,1,2]
Output: [1]

```

 **Example 3:** 

```
Input: nums = [1]
Output: []

```

 

 **Constraints:** 

- n == nums.length
- 1 <= n <= 105
- 1 <= nums[i] <= n
- Each element in nums appears once or twice.

## Solution

**Language:** Python  
**Runtime:** 56 ms (beats 7.22%)  
**Memory:** 29.4 MB (beats 90.57%)  
**Submitted:** 2026-10-25T05:46:41.238Z  

```py
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
                
        
```

---

[View on LeetCode](https://leetcode.com/problems/find-all-duplicates-in-an-array/)