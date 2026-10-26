class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        l = 0
        r = len(s) - 1
        spaces_set = set(spaces)
        left_result = []
        right_result = []
        
        while l <= r:
            if l in spaces_set:
                left_result.append(' ')
            left_result.append(s[l])
            if l != r:
                right_result.append(s[r])
                if r in spaces_set:
                    right_result.append(' ')
            
            l += 1
            r -= 1
        return "".join(left_result) + "".join(reversed(right_result))