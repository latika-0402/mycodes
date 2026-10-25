# Palindrome Number

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer `x`, return `true` if `x` is a  **palindrome**, and `false` otherwise.

 

 **Example 1:** 

```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

```

 **Example 2:** 

```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

```

 **Example 3:** 

```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

```

 

 **Constraints:** 

- -231 <= x <= 231 - 1

 

 **Follow up:**  Could you solve it without converting the integer to a string?

## Solution

**Language:** Python  
**Runtime:** 18 ms (beats 12.54%)  
**Memory:** 19.1 MB (beats 95.98%)  
**Submitted:** 2026-10-25T08:24:29.202Z  

```py
class Solution:
    def isPalindrome(self, x: int) -> bool:
        digit_list = [digit for digit in str(x)]
        l=0
        r=len(digit_list)-1
        while l<r:
            digit_list[l],digit_list[r]=digit_list[r],digit_list[l]
            l+=1
            r-=1
        if str(x)=="".join(digit_list):return True
        else:return False

        
```

---

[View on LeetCode](https://leetcode.com/problems/palindrome-number/)