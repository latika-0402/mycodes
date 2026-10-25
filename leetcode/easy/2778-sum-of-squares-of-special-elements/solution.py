class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i, num in enumerate(nums, start=1):
            if n % i == 0:
                result += num * num
        return result
        