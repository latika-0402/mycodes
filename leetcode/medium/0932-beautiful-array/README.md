# Beautiful Array

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

An array `nums` of length `n` is  **beautiful**  if:

- nums is a permutation of the integers in the range [1, n].
- For every 0 <= i < j < n, there is no index k with i < k < j where 2 * nums[k] == nums[i] + nums[j].

Given the integer `n`, return  *any  **beautiful**  array* `nums` *of length* `n`. There will be at least one valid answer for the given `n`.

 

 **Example 1:** 

```
Input: n = 4
Output: [2,1,4,3]

```

 **Example 2:** 

```
Input: n = 5
Output: [3,1,2,5,4]

```

 

 **Constraints:** 

- 1 <= n <= 1000

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.2 MB (beats 72.53%)  
**Submitted:** 2026-10-29T02:40:52.743Z  

```py
class Solution:
    def recurse(self, nums):
        if len(nums) <= 2: return nums
        return self.recurse(nums[::2]) + self.recurse(nums[1::2])
    
    def beautifulArray(self, n: int) -> List[int]:
        return self.recurse([i for i in range(1, n+1)])
```

---

[View on LeetCode](https://leetcode.com/problems/beautiful-array/)