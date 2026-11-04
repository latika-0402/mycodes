# Word Break

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

 **Note**  that the same word in the dictionary may be reused multiple times in the segmentation.

 

 **Example 1:** 

```
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

```

 **Example 2:** 

```
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

```

 **Example 3:** 

```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

```

 

 **Constraints:** 

- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- s and wordDict[i] consist of only lowercase English letters.
- All the strings of wordDict are unique.

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 81.75%)  
**Memory:** 19.3 MB (beats 74.12%)  
**Submitted:** 2026-11-04T08:36:17.433Z  

```py
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [True] + [False] * len(s)

        for i in range(1, len(s) + 1):
            for w in wordDict:
                start = i - len(w)
                if start >= 0 and dp[start] and s[start:i] == w:
                    dp[i] = True
                    break
        
        return dp[-1]
        
```

---

[View on LeetCode](https://leetcode.com/problems/word-break/)