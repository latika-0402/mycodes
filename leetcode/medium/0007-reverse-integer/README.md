# Reverse Integer

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a signed 32-bit integer `x`, return `x` *with its digits reversed*. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-231, 231 - 1]`, then return `0`.

 **Assume the environment does not allow you to store 64-bit integers (signed or unsigned).** 

 

 **Example 1:** 

```
Input: x = 123
Output: 321

```

 **Example 2:** 

```
Input: x = -123
Output: -321

```

 **Example 3:** 

```
Input: x = 120
Output: 21

```

 

 **Constraints:** 

- -231 <= x <= 231 - 1

## Solution

**Language:** Python  
**Runtime:** 2 ms (beats 50.94%)  
**Memory:** 19.1 MB (beats 94.98%)  
**Submitted:** 2026-10-28T08:53:25.480Z  

```py
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        digit_list = list(str(abs(x)))
        l, r = 0, len(digit_list) - 1
        while l < r:
            digit_list[l], digit_list[r] = digit_list[r], digit_list[l]
            l += 1
            r -= 1
        rev = int("".join(digit_list)) * sign
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev

        
```

---

[View on LeetCode](https://leetcode.com/problems/reverse-integer/)