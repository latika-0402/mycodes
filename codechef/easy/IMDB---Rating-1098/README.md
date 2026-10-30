# IMDB - Rating 1098

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Motivation
### Read problem statements in Russian

Chef has been searching for a good motivational movie that he can watch during his exam time. His hard disk has $X$ GB of space remaining. His friend has $N$ movies represented with $(S_i, R_i)$ representing (space required, IMDB rating). Help Chef choose the single best movie (highest IMDB rating) that can fit in his hard disk.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $X$.
- $N$ lines follow. For each valid $i$, the $i$-th of these lines contains two space-separated integers $S_i$ and $R_i$.
### Output

For each test case, print a single line containing one integer - the highest rating of an IMDB movie which Chef can store in his hard disk.

### Constraints
- $1 \leq T \leq 10$
- $1 \leq N \leq 5 \cdot 10^4$
- $1 \leq X \leq 10^9$
- $1 \leq S_i, R_i \leq 10^9$ for each valid $i$
- $X \ge S_i$ for atleast one valid $i$
### Subtasks

 **Subtask #1 (100 points):**  original constraints

### Sample 1:
Input
Output

```
3
1 1
1 1
2 2
1 50
2 100
3 2
1 51
3 100
2 50
```

```
1
100 
51
```

### Explanation:

 **Example case 1:**  Since there is only $1$ movie available and requires space equivalent to the empty space in the hard disk, Chef can only obtain maximum IMDB rating of $1$.

 **Example case 2:**  Since out of the $2$ available movies, both can fit in the free memory, we only care to take the one with higher rating, i.e, rating of $max(50, 100) = 100$.

 **Example case 3:**  Since out of the $3$ available movies, only the first and the last movies fit in the free memory, we only care to take the one with higher rating amongst these $2$, i.e, rating of $\max(51, 50) = 51$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-30T15:58:24.868Z  

```py
# cook your dish here
# cook your dish here
t=int(input())
for _ in range(t):
    n, x = map(int, input().split())
    max_rating = 0
    for _ in range(n):
        s, r = map(int, input().split())
        if s <= x and r > max_rating:
            max_rating = r
    print(max_rating)
```

---

[View on CodeChef](https://www.codechef.com/problems/IMDB)