# CHFSPL - Rating 965

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-31T04:36:36.951Z  

```py
# cook your dish here
# cook your dish here
t = int(input())
for _ in range(t):
    a, b, a1, b1, a2, b2 = map(int, input().split())
    required = {a, b}
    lang1 = {a1, b1}
    lang2 = {a2, b2}
    if required.issubset(lang1):
        print(1)
    elif required.issubset(lang2):
        print(2)
    else:
        print(0)
```

---

[View on CodeChef](https://www.codechef.com/problems/CHFSPL)