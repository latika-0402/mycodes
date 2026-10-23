# TODOLIST - Rating 578

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T08:40:12.769Z  

```py
# cook your dish here
# cook your dish here
t = int(input())
for _ in range(t):
    profits = list(map(int, input().split()))
    max_profit = max(profits)
    total_profit = sum(profits)
    if max_profit > total_profit - max_profit:
        print("YES")
    else:
        print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/TODOLIST)