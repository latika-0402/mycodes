# FLOW017 - Rating 728

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-27T13:04:53.002Z  

```py
# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    score_ab = (500 - 2 * x) + (1000 - 4 * (x + y))
    score_ba = (1000 - 4 * y) + (500 - 2 * (y + x))
    print(max(score_ab, score_ba))
```

---

[View on CodeChef](https://www.codechef.com/problems/FLOW017)