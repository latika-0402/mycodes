# PRB01 - Rating 793

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-28T12:59:45.083Z  

```py
# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    codes = input().split()
    
    start38_count = codes.count("START38")
    ltime108_count = codes.count("LTIME108")
    
    print(start38_count, ltime108_count)
```

---

[View on CodeChef](https://www.codechef.com/problems/PRB01)