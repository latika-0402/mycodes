# Count Sorted Vowel Strings

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer `n`, return  *the number of strings of length* `n` *that consist only of vowels (* `a` *,* `e` *,* `i` *,* `o` *,* `u` *) and are  **lexicographically sorted**.* 

A string `s` is  **lexicographically sorted**  if for all valid `i`, `s[i]` is the same as or comes before `s[i+1]` in the alphabet.

 

 **Example 1:** 

```
Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].

```

 **Example 2:** 

```
Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.

```

 **Example 3:** 

```
Input: n = 33
Output: 66045

```

 

 **Constraints:** 

- 1 <= n <= 50

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.3 MB (beats 61.75%)  
**Submitted:** 2026-10-25T06:09:19.460Z  

```py
class Solution:
    def countVowelStrings(self, n: int) -> int:
        def fact(n):
            if n==0 or n==1:return 1
            else:return n*fact(n-1)
        r=5
        return int(fact(n+r-1)/(fact(n)*fact(r-1)))
        
```

---

[View on LeetCode](https://leetcode.com/problems/count-sorted-vowel-strings/)