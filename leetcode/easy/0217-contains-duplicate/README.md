# Contains Duplicate

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array `nums`, return `true` if any value appears  **at least twice**  in the array, and return `false` if every element is distinct.

 

 **Example 1:** 

 **Input:**  nums = [1,2,3,1]

 **Output:**  true

 **Explanation:** 

The element 1 occurs at the indices 0 and 3.

 **Example 2:** 

 **Input:**  nums = [1,2,3,4]

 **Output:**  false

 **Explanation:** 

All elements are distinct.

 **Example 3:** 

 **Input:**  nums = [1,1,1,3,3,4,3,2,4,2]

 **Output:**  true

 

 **Constraints:** 

- 1 <= nums.length <= 105
- -109 <= nums[i] <= 109

## Solution

**Language:** Python  
**Runtime:** 60 ms (beats 5.13%)  
**Memory:** 33.2 MB (beats 19.49%)  
**Submitted:** 2026-10-31T15:50:02.122Z  

```py
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        seen=set()
        for i in nums:
            if i in seen:return True
            seen.add(i)
        return False
        
```

---

[View on LeetCode](https://leetcode.com/problems/contains-duplicate/)