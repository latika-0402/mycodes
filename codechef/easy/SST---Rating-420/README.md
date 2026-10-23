# SST - Rating 420

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T12:22:40.362Z  

```py
# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    result=0
    while n>0:
        rem=n%10
        result=result*10+rem
        n=n//10
    print(result)
```

---

[View on CodeChef](https://www.codechef.com/problems/SST)