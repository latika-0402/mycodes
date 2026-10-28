# MOZZ - Rating 745

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-28T09:38:09.662Z  

```py
# cook your dish here
t=int(input())
for _ in range(t):
    x,y,a,b=map(int,input().split())
    count = 0
    if x != a and x != b:
            count += 1
    
    if y != a and y != b:
            count += 1
    print(count)
```

---

[View on CodeChef](https://www.codechef.com/problems/MOZZ)