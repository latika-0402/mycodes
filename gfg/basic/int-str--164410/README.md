# String Repetition and Separation in Python

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given three inputs  **a**,  **b**, and  **c**, print a exactly a times and b exactly b times in the same line, with c printed between them.

 **Examples:** 

```
Input: a = 6, b = 4, c = &
Output: 666666&4444
Explanation: 6 printed 6 times and 4 printed 4 times separated by c = &.
```

```
Input: a = 1, b = 3, c = #
Output: 1#333
Explanation: 1 is printed once and 3 is printed 3 times, with # between them.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-25T14:08:59.689Z  

```py
a = input()
b = input()
c = input()

# code here
print((a*int(a))+c+(b*int(b)))
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/int-str--164410/1)