# TLG - Rating 789

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-28T12:54:43.009Z  

```py
# cook your dish here
t=int(input())
for _ in range(t):
    a,b,c,d,e,f=map(int,input().split())
    alice=a+b+c-min(a,b,c)
    bob=d+e+f-min(d,e,f)
    if alice>bob:print("Alice")
    elif alice<bob:print("Bob")
    else:print("Tie")
```

---

[View on CodeChef](https://www.codechef.com/problems/TLG)