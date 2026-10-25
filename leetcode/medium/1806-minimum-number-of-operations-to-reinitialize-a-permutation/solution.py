class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = [i for i in range(n)]
        initial = list(perm)
        arr = [0] * n
        operations = 0
        
        while True:
            for i in range(n):
                if i % 2 == 0:
                    arr[i] = perm[i // 2]
                else:
                    arr[i] = perm[n // 2 + (i - 1) // 2]
            
            perm = list(arr)
            operations += 1
            if perm == initial:
                return operations