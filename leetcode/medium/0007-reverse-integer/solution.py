class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        digit_list = list(str(abs(x)))
        l, r = 0, len(digit_list) - 1
        while l < r:
            digit_list[l], digit_list[r] = digit_list[r], digit_list[l]
            l += 1
            r -= 1
        rev = int("".join(digit_list)) * sign
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev

        