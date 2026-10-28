# CHN15A - Rating 970

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-28T09:52:58.787Z  

```py
# cook your dish here
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if a>b:print(">")
    elif a<b:print("<")
    else:print("=")
```

---

[View on CodeChef](https://www.codechef.com/problems/CHN15A)