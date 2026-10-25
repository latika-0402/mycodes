# Print Hollow Square

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given an integer  **n**, print the hollow square pattern of size  **n**  using  **'*'** character **.** 

 **Examples:** 

```
Input: n = 4
Output:
 **   ** 
 ** 
 ** 
 **   ** 
Explanation: It's a hollow square! Each side contains n = 4.

```

```
Input: n = 3
Output:
 **  * 
 ** 
 **  *
Explanation: It's a hollow square! Each side contains n = 3.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-25T14:05:54.864Z  

```py
class Solution:
    def printHollowSquare(self, n):
        # code here
        for i in range(n):
            for j in range(n):
                if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                                    print("*", end=" ")
                else:
                                    print(" ", end=" ")
            print()
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/print-square--105330/1)