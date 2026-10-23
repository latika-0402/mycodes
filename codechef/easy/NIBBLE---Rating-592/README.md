# NIBBLE - Rating 592

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T12:25:31.372Z  

```py
# cook your dish here
# cook your dish here
t = int(input())
for _ in range(t):
    A, B = map(int, input().split())
    
    # Calculate company valuations
    val1 = A * 10
    val2 = B * 5
    
    if val1 > val2:
        print("FIRST")
    elif val2 > val1:
        print("SECOND")
    else:
        print("ANY")
```

---

[View on CodeChef](https://www.codechef.com/problems/NIBBLE)