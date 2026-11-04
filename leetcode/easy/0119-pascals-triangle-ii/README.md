# Pascal's Triangle II

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer `rowIndex`, return the `rowIndexth` (**0-indexed**) row of the  **Pascal's triangle**.

In  **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

 

 **Example 1:** 

```
Input: rowIndex = 3
Output: [1,3,3,1]

```

 **Example 2:** 

```
Input: rowIndex = 0
Output: [1]

```

 **Example 3:** 

```
Input: rowIndex = 1
Output: [1,1]

```

 

 **Constraints:** 

- 0 <= rowIndex <= 33

 

 **Follow up:**  Could you optimize your algorithm to use only `O(rowIndex)` extra space?

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.3 MB (beats 51.64%)  
**Submitted:** 2026-11-04T08:39:58.370Z  

```py
class Solution(object):
    def getRow(self, rowIndex):
        row = [1]

        for _ in range(rowIndex):
            row = [left + right for left, right in zip([0]+row, row+[0])]
            
        return row    
```

---

[View on LeetCode](https://leetcode.com/problems/pascals-triangle-ii/)