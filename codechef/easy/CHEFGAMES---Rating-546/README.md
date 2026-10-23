# CHEFGAMES - Rating 546

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T08:38:59.768Z  

```py
# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    total_slices = x * y
    print((total_slices + 3) // 4)
```

---

[View on CodeChef](https://www.codechef.com/problems/CHEFGAMES)