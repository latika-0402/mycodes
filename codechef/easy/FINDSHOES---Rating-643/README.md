# FINDSHOES - Rating 643

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T15:35:11.458Z  

```py
# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    required=2*y
    if 2*y<=x:
        print(x//(required))
    else:print(0)
```

---

[View on CodeChef](https://www.codechef.com/problems/FINDSHOES)