# Letter Tile Possibilities

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You have `n`  `tiles`, where each tile has one letter `tiles[i]` printed on it.

Return  *the number of possible non-empty sequences of letters*  you can make using the letters printed on those `tiles`.

 

 **Example 1:** 

```
Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

```

 **Example 2:** 

```
Input: tiles = "AAABBC"
Output: 188

```

 **Example 3:** 

```
Input: tiles = "V"
Output: 1

```

 

 **Constraints:** 

- 1 <= tiles.length <= 7
- tiles consists of uppercase English letters.

## Solution

**Language:** Python  
**Runtime:** 33 ms (beats 59.55%)  
**Memory:** 19.3 MB (beats 84.39%)  
**Submitted:** 2026-10-29T02:44:33.026Z  

```py
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counter = collections.Counter(tiles)
        
        def backtrack():
            total = 0
            for char in counter:
                if counter[char] > 0:
                    # Choose this character
                    counter[char] -= 1
                    total += 1 + backtrack()
                    # Backtrack (undo choice)
                    counter[char] += 1
            return total
            
        return backtrack()
```

---

[View on LeetCode](https://leetcode.com/problems/letter-tile-possibilities/)