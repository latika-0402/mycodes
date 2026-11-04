# OPMIN - Rating 928

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-04T07:33:25.154Z  

```py
t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1
    # Your code goes here
    unique_a = list(set(a))
    unique_a.sort()
    
    print(unique_a[-1] + unique_a[-2])
```

---

[View on CodeChef](https://www.codechef.com/problems/OPMIN)