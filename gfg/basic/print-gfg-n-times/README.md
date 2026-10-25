# Print GFG n times

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given a positive number  **n**, print the string " **GFG** " exactly n times separated by a single space.

 **Examples:** 

```
Input: n = 5
Output: GFG GFG GFG GFG GFG
Explanation: The string "GFG" is printed 5 times, with each instance separated by a space.
```

```
Input: 3
Output: GFG GFG GFG
Explanation: The string "GFG" is printed 3 times separated by spaces.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-25T14:02:30.784Z  

```py
class Solution:
    def printGfg(self, n: int) -> None:
        for i in range(n):
            print("GFG",end=' ')
        
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/print-gfg-n-times/1)