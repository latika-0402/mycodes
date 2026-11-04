# Majority Element II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array of size `n`, find all elements that appear more than `⌊n / 3⌋` times.

 

 **Example 1:** 

```
Input: nums = [3,2,3]
Output: [3]

```

 **Example 2:** 

```
Input: nums = [1]
Output: [1]

```

 **Example 3:** 

```
Input: nums = [1,2]
Output: [1,2]

```

 

 **Constraints:** 

- 1 <= nums.length <= 5 * 104
- -109 <= nums[i] <= 109

 

 **Follow up:**  Could you solve the problem in linear time and in `O(1)` space?

## Solution

**Language:** Python  
**Runtime:** 7 ms (beats 66.01%)  
**Memory:** 23.5 MB (beats 37.68%)  
**Submitted:** 2026-11-04T08:45:47.383Z  

```py
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n=len(nums)
        result=[]
        d=collections.Counter(nums)
        for i,j in d.items():
            if j>n//3:
                result.append(i)
        return result
```

---

[View on LeetCode](https://leetcode.com/problems/majority-element-ii/)