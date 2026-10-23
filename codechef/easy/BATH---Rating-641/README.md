# BATH - Rating 641

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T15:31:33.349Z  

```py
# cook your dish here
t=int(input())
for _ in range(t):
    c,f=map(int,input().split())
    if f==0 or c==f:
        print(0)
    else:print(min(f,c-f))
```

---

[View on CodeChef](https://www.codechef.com/problems/BATH)