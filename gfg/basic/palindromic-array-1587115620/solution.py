class Solution:
    def isPalinArray(self, arr):
         # code here
         return all(str(x) == str(x)[::-1] for x in arr)