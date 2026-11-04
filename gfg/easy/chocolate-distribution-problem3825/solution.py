class Solution:
    def findMinDiff(self, arr, m):
        if m == 0 or len(arr) == 0:
            return 0
        if len(arr) < m:
            return -1
        arr.sort()
        min_diff = float('inf')
        for i in range(len(arr) - m + 1):
            diff = arr[i + m - 1] - arr[i]
            if diff < min_diff:
                min_diff = diff

        return min_diff