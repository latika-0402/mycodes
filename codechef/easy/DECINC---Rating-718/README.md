# DECINC - Rating 718

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-26T14:41:02.939Z  

```py
# cook your dish here
t=int(input())
for _ in range(t):
    a,x,b,y=map(int,input().split())
    if a/x == b/y :print("Equal")
    elif a/x > b/y : print("Alice")
    else:print("Bob")
```

---

[View on CodeChef](https://www.codechef.com/problems/DECINC)