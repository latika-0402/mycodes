class Solution:
    def reverseDegree(self, s: str) -> int:
        j = 1
        total = 0
        for i in s:
            reversed_alpha = 27 - (ord(i) - ord('a') + 1)
            total += reversed_alpha * j
            j += 1
            
        return total
        