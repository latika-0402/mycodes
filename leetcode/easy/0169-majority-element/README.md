# Majority Element

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an array `nums` of size `n`, return  *the majority element*.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

 

 **Example 1:** 

```
Input: nums = [3,2,3]
Output: 3

```

 **Example 2:** 

```
Input: nums = [2,2,1,1,1,2,2]
Output: 2

```

 

 **Constraints:** 

- n == nums.length
- 1 <= n <= 5 * 104
- -109 <= nums[i] <= 109
- The input is generated such that a majority element will exist in the array.

 

 **Follow-up:**  Could you solve the problem in linear time and in `O(1)` space?

## Solution

**Language:** Python  
**Runtime:** 11 ms (beats 56.97%)  
**Memory:** 21.5 MB (beats 68.59%)  
**Submitted:** 2026-10-31T07:46:49.924Z  

```py
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        d=collections.Counter(nums)
        for i,j in d.items():
            if j>len(nums)//2:
                return i
        
```

---

[View on LeetCode](https://leetcode.com/problems/majority-element/)