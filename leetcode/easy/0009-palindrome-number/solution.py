class Solution:
    def isPalindrome(self, x: int) -> bool:
        digit_list = [digit for digit in str(x)]
        l=0
        r=len(digit_list)-1
        while l<r:
            digit_list[l],digit_list[r]=digit_list[r],digit_list[l]
            l+=1
            r-=1
        if str(x)=="".join(digit_list):return True
        else:return False

        