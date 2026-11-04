class Solution:
    def rotate(self, arr: list[int]) -> None:
        # code here
       if arr:
           arr[:] = arr[-1:] + arr[:-1]