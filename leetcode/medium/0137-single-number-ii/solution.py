class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones = 0
        twos = 0
        
        for num in nums:
            # Update 'ones': bits that appear 1 time (or 4, 7, etc.)
            ones = (ones ^ num) & ~twos
            # Update 'twos': bits that appear 2 times (or 5, 8, etc.)
            twos = (twos ^ num) & ~ones
            
        return ones