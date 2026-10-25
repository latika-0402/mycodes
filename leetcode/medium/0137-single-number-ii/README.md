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
**Runtime:** 2 ms (beats 78.60%)  
**Memory:** 21.4 MB (beats 8.43%)  
**Submitted:** 2026-10-25T16:17:36.360Z  

```py
from collections import Counter
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        h=Counter(nums)
        for i,j in h.items():
            if j==1:
                return i
        
        
```

---

[View on LeetCode](https://leetcode.com/problems/single-number-ii/)