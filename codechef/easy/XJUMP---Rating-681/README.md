# XJUMP - Rating 681

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-24T12:00:02.419Z  

```py
# cook your dish here
t=int(input())
for _ in range(t):
    n,k,m=map(int,input().split())
    print((n + (k * m) - 1) // (k * m))
```

---

[View on CodeChef](https://www.codechef.com/problems/XJUMP)