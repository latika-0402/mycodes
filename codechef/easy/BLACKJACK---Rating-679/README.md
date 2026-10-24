# BLACKJACK - Rating 679

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-24T11:46:22.752Z  

```py
# cook your dish here
t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    play=x*y
    breaks=(x-1)//3
    bt=breaks*z
    print(play+bt)
```

---

[View on CodeChef](https://www.codechef.com/problems/BLACKJACK)