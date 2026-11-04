# Array with All Palindromes

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given an array  **arr[]**  of positive integers. Return true if all the array elements are palindrome otherwise, return false.

 **Examples:** 

```
Input: arr[] = [111, 222, 333, 444, 555]
Output: true
Explanation:
arr[0] = 111, which is a palindrome number.
arr[1] = 222, which is a palindrome number.
arr[2] = 333, which is a palindrome number.
arr[3] = 444, which is a palindrome number.
arr[4] = 555, which is a palindrome number.
As all numbers are palindrome so This will return true.
```

```
Input: arr[] = [121, 131, 20]
Output: false
Explanation: 20 is not a palindrome hence the output is false.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-04T12:51:40.596Z  

```py
class Solution:
    def isPalinArray(self, arr):
         # code here
         return all(str(x) == str(x)[::-1] for x in arr)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/palindromic-array-1587115620/1)