# Taking Input

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

You need to perform three separate tasks based on the given input:

- String Input and Print: Read a string s (which may contain spaces) and print it as it is.
- Integer Input and Print: Read an integer n and print it without any change.
- Float Input and floor Print: Read a floating-point number as input, take its floor value, and print as an integer.

 **Examples:** 

```
Input: s = "Hello", n = 20, f = 5.5
Output: 
Hello
20
5
Explanation: 
The string Hello is printed as it is.
The integer 20 is printed without any change.
For floating-point number 5.5, its floor value 5 is printed.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-25T13:51:38.031Z  

```py
import math

# s to store string
# n to store integer
# f to store float
# ff  # To Store floor of float variable f

# code here
s=input()
n=int(input())
f=float(input())
print(s)
print(n)
print(int(f))

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/taking-input/1)