# MINFLIPS - Rating 778

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-28T12:43:29.008Z  

```py
# cook your dish here
t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    sumval = (a + b + c) - min(a, b, c)
    print(sumval)
    
```

---

[View on CodeChef](https://www.codechef.com/problems/MINFLIPS)