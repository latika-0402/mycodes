class Solution:
    def countVowelStrings(self, n: int) -> int:
        def fact(n):
            if n==0 or n==1:return 1
            else:return n*fact(n-1)
        r=5
        return int(fact(n+r-1)/(fact(n)*fact(r-1)))
        