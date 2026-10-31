# Count Primes

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer `n`, return  *the number of prime numbers that are strictly less than*  `n`.

 

 **Example 1:** 

```
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

```

 **Example 2:** 

```
Input: n = 0
Output: 0

```

 **Example 3:** 

```
Input: n = 1
Output: 0

```

 

 **Constraints:** 

- 0 <= n <= 5 * 106

## Solution

**Language:** Python  
**Runtime:** 1496 ms (beats 90.31%)  
**Memory:** 65.9 MB (beats 78.11%)  
**Submitted:** 2026-10-31T15:42:48.304Z  

```py
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:return 0
        primes=[True]*n
        primes[0] = primes[1] = False
        for i in range(2,int(n**0.5)+1):
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = False
        return sum(primes)


        
```

---

[View on LeetCode](https://leetcode.com/problems/count-primes/)