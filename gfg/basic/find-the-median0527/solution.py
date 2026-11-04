class Solution:
    def findMedian(self, arr):
        arr.sort()
        n = len(arr)
        #code here.
        if len(arr)%2==1:
            return arr[n//2]
        else:
            return (arr[(n // 2) - 1] + arr[n // 2]) / 2.0