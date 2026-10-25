# Single Number II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums` where every element appears  **three times**  except for one, which appears  **exactly once**.  *Find the single element and return it*.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

 **Example 1:** 

```
Input: nums = [2,2,3,2]
Output: 3

```

 **Example 2:** 

```
Input: nums = [0,1,0,1,0,1,99]
Output: 99

```

 

 **Constraints:** 

- 1 <= nums.length <= 3 * 104
- -231 <= nums[i] <= 231 - 1
- Each element in nums appears exactly three times except for one element which appears once.

## Solution

**Language:** Python  
**Runtime:** 5 ms (beats 39.31%)  
**Memory:** 20.9 MB (beats 18.35%)  
**Submitted:** 2026-10-25T16:14:50.430Z  

```py
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones = 0
        twos = 0
        
        for num in nums:
            # Update 'ones': bits that appear 1 time (or 4, 7, etc.)
            ones = (ones ^ num) & ~twos
            # Update 'twos': bits that appear 2 times (or 5, 8, etc.)
            twos = (twos ^ num) & ~ones
            
        return ones
```

---

[View on LeetCode](https://leetcode.com/problems/single-number-ii/)