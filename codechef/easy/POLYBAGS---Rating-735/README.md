# POLYBAGS - Rating 735

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-27T13:23:54.966Z  

```py
# cook your dish here
t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    if a + c == 180:
        print("YES")
    else:
        print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/POLYBAGS)