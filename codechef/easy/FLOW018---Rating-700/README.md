# FLOW018 - Rating 700

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Small Factorial

Write a program to find the factorial value of any number entered by the user.

### Input Format

The first line contains an integer  **T**, the total number of testcases. Then  **T**  lines follow, each line contains an integer  **N**.

### Output Format

For each test case, display the factorial of the given number  **N**  in a new line.

### Constraints
- 1 ≤ T ≤ 1000
- 0 ≤ N ≤ 20
### Sample 1:
Input
Output

```
3 
3 
4
5

```

```
6
24
120

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-28T09:44:30.296Z  

```py
# cook your dish here
def fact(n):
    if n==1 or n==0:return 1
    else: return n*fact(n-1)
t=int(input())
for _ in range(t):
    n=int(input())
    print(fact(n))
```

---

[View on CodeChef](https://www.codechef.com/problems/FLOW018)