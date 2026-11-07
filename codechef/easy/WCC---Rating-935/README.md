# WCC - Rating 935

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### World Chess Championship

The World Chess Championship $2022$ is about to start. $14$ Classical games will be played between Chef and Carlsen in the championship, where each game has one of three outcomes — it can be won by Carlsen, won by Chef, or it can be a draw. The winner of a game gets $2$ points, and the loser gets $0$ points. If it’s a draw, both players get $1$ point each.

The total prize pool of the championship is $100 \cdot X$. At end of the $14$ Classical games, if one player has  **strictly more**  points than the other, he is declared the champion and gets $60 \cdot X$ as his prize money, and the loser gets $40 \cdot X$.

If the total points are  **tied**, then the defending champion Carlsen is declared the winner. However, if this happens, the winner gets only $55 \cdot X$, and the loser gets $45 \cdot X$.

Given the results of all the $14$ games, output the prize money that Carlsen receives.

The results are given as a string of length $14$ consisting of the characters `C`, `N`, and `D`.

- C denotes a victory by Carlsen.
- N denotes a victory by Chef.
- D denotes a draw.
### Input Format
- The first line of input contains an integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains one integer $X$, denoting that the total prize pool is $100\cdot X$.
- The second line contains the results of the match, as a string of length $14$ containing only the characters C, N, and D.
### Output Format

For each test case, output in a single line the total prize money won by Carlsen.

### Constraints
- $1 \leq T \leq 1000$
- $1 \leq X \leq 10^6$
- $|S| = 14$
- $S$ contains only characters D, C, N.
### Subtasks

 **Subtask #1 (100 points):**  Original constraints

### Sample 1:
Input
Output

```
4
100
CCCCCCCCCCCCCC
400
CDCDCDCDCDCDCD
30
DDCCNNDDDCCNND
1
NNDNNDDDNNDNDN
```

```
6000
24000
1650
40

```

### Explanation:

 **Test case $1$:**  Since Carlsen won all the games, he will be crowned the champion and will get $60 \cdot X$ as the prize money which is $60 \cdot 100 = 6000$

 **Test case $2$:**  Carlsen won $7$ games and drew $7$, so his score is $2 \cdot 7 + 1 \cdot 7 = 21$. Chef lost $7$ games and drew $7$, so his score is $0 \cdot 7 + 1 \cdot 7 = 7$. Since Carlsen has more points, he will be crowned the champion and will get $60 \cdot X$ as the prize money which is $60 \cdot 400 = 24000$

 **Test case $3$:**  Carlsen and Chef both end up with $14$ points. So, Carlsen is declared the winner, but because the points were tied, he receives $55\cdot X = 55\cdot 30 = 1650$ in prize money.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-07T14:02:11.883Z  

```py
# cook your dish here
import sys


def solve():
  input_data = sys.stdin.read().split()
  if not input_data:
    return

  t = int(input_data[0])
  idx = 1

  for _ in range(t):
    x = int(input_data[idx])
    s = input_data[idx + 1]
    idx += 2

    carlsen_points = 0
    chef_points = 0

    for char in s:
      if char == "C":
        carlsen_points += 2
      elif char == "N":
        chef_points += 2
      elif char == "D":
        carlsen_points += 1
        chef_points += 1

    if carlsen_points > chef_points:
      print(60 * x)
    elif chef_points > carlsen_points:
      print(40 * x)
    else:
      # Tie: Carlsen is the defending champion and wins even if tied
      print(55 * x)


if __name__ == "__main__":
  solve()
```

---

[View on CodeChef](https://www.codechef.com/problems/WCC)