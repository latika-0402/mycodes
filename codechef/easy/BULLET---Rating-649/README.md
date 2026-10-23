# BULLET - Rating 649

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T15:47:40.409Z  

```py
# cook your dish here
# cook your dish here
t = int(input())
for _ in range(t):
    x = int(input())
    
    # Check the remainder when divided by 3
    if x % 3 == 1:
        print("HUGE")
    elif x % 3 == 2:
        print("SMALL")
    else:
        print("NORMAL")
```

---

[View on CodeChef](https://www.codechef.com/problems/BULLET)