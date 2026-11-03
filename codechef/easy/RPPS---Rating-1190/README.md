# RPPS - Rating 1190

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Repeating Pairs

You are given a string $S$ consisting of lowercase English letters.

For every two adjacent characters in $S$, consider the pair they form. For example, the string `abca` contains the pairs `ab`, `bc`, and `ca`.

A pair is called  **repeating**  if it appears at least twice in the string.

Find the  **number of distinct repeating pairs**  in $S$.

For example, in `ababcabc`, the pair `ab` appears $3$ times and `bc` appears $2$ times, so the answer is $2$.

### Input Format
- The first line contains the string $S$.
### Output Format
- Print a single integer — the number of distinct consecutive character pairs that appear more than once.
### Constraints
- $1 \le |S| \le 10^5$
- $S$ consists only of lowercase English letters.
### Sample 1:
Input
Output

```
ababcabc
```

```
2
```

### Explanation:

The consecutive pairs are:

`ab`, `ba`, `ab`, `bc`, `ca`, `ab`, `bc`

The pair `ab` appears $3$ times and `bc` appears $2$ times.

Therefore, there are  **2**  distinct repeating pairs.

### Sample 2:
Input
Output

```
aaaa
```

```
1
```

### Explanation:

The consecutive pairs are:

`aa`, `aa`, `aa`

Only the pair `aa` appears more than once.

Therefore, the answer is  **1**.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-03T15:45:47.412Z  

```py
# cook your dish here
# cook your dish here
s = input().strip()

# Dictionary to store the frequency of each consecutive pair
counts = {}

for i in range(len(s) - 1):
  pair = s[i] + s[i + 1]
  if pair in counts:
    counts[pair] += 1
  else:
    counts[pair] = 1

# Count how many pairs appear at least twice
ans = 0
for pair in counts:
  if counts[pair] >= 2:
    ans += 1

print(ans)
```

---

[View on CodeChef](https://www.codechef.com/problems/RPPS)