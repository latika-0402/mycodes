# PROGLANG - Rating 1001

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Programming Languages

Chef is a software developer, so he has to switch between different languages sometimes. Each programming language has some features, which are represented by integers here.

Currently, Chef has to use a language with two given features $A$ and $B$. He has two options --- switching to a language with two features $A_1$ and $B_1$, or to a language with two features $A_2$ and $B_2$. All four features of these two languages are pairwise distinct.

Tell Chef whether he can use the first language, the second language or neither of these languages (if no single language has all the required features).

### Input Format
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains six space-separated integers $A, B, A_1, B_1, A_2, B_2$.
### Output Format

For each test case, print a single line containing the integer $1$ if Chef should switch to the first language, or $2$ if Chef should switch to the second language, or $0$ if Chef cannot switch to either language.

### Constraints
- $1 \leq T \leq 288$
- $1 \leq A, B, A_1, B_1, A_2, B_2 \leq 4$
- $A, B$ are distinct
- $A_1, B_1, A_2, B_2$ are pairwise distinct
### Subtasks

 **Subtask #1 (100 points):**  original constraints

### Sample 1:
Input
Output

```
3
1 2 2 1 3 4
3 4 2 1 4 3
1 2 1 3 2 4
```

```
1
2
0
```

### Explanation:

 **Example case 1:**  The first language has the required features --- features $1$ and $2$.

 **Example case 2:**  The second language has the required features --- features $3$ and $4$.

 **Example case 3:**  Neither language has both features $1$ and $2$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-31T04:36:21.524Z  

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

[View on CodeChef](https://www.codechef.com/problems/PROGLANG)