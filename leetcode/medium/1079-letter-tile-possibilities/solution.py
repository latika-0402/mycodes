class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counter = collections.Counter(tiles)
        
        def backtrack():
            total = 0
            for char in counter:
                if counter[char] > 0:
                    # Choose this character
                    counter[char] -= 1
                    total += 1 + backtrack()
                    # Backtrack (undo choice)
                    counter[char] += 1
            return total
            
        return backtrack()