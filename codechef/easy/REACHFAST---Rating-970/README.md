# REACHFAST - Rating 970

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-28T09:56:58.652Z  

```py
# cook your dish here
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    count=0
    result=[i+k for i in l]
    for i in result:
        if i%7==0:count+=1
    print(count)
```

---

[View on CodeChef](https://www.codechef.com/problems/REACHFAST)