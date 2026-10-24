# WTRMIXING - Rating 691

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-24T12:10:09.754Z  

```py
# cook your dish here
t = int(input())
for _ in range(t):
    p, q = map(int, input().split())
    total_points = p + q
    if (total_points // 2) % 2 == 0:
        print("Alice")
    else:
        print("Bob")
```

---

[View on CodeChef](https://www.codechef.com/problems/WTRMIXING)