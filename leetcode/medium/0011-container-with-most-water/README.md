# Container With Most Water

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return  *the maximum amount of water a container can store*.

 **Notice**  that you may not slant the container.

 

 **Example 1:** 

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

```

 **Example 2:** 

```
Input: height = [1,1]
Output: 1

```

 

 **Constraints:** 

- n == height.length
- 2 <= n <= 105
- 0 <= height[i] <= 104

## Solution

**Language:** Python  
**Runtime:** 60 ms (beats 38.04%)  
**Memory:** 29.7 MB (beats 39.74%)  
**Submitted:** 2026-10-25T16:03:54.670Z  

```py
class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_result=0
        l=0
        r=len(height)-1
        while l<r:
            w=r-l
            current_height = min(height[l], height[r])
            current_area = w * current_height
            max_result=max(max_result,current_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_result

        
```

---

[View on LeetCode](https://leetcode.com/problems/container-with-most-water/)