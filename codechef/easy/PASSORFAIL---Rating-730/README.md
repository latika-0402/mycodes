# PASSORFAIL - Rating 730

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-27T13:09:02.270Z  

```py
# cook your dish here
t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    nums=[a,b,c]
    first=second=-1
    for i in nums:
        if i>first:
            second=first
            first=i
        elif i>second:second=i
    print(second)
```

---

[View on CodeChef](https://www.codechef.com/problems/PASSORFAIL)