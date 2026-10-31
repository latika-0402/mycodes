class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        result = int("".join(map(str, digits))) +1
        return [int(char) for char in str(result)]
        