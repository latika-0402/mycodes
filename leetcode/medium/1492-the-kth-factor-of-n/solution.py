class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        result=[]
        for i in range(1,n+1):
            if n%i==0:
                result.append(i)
                if len(result)==k:
                    break
        if len(result)<k:return -1
        return result[-1]

        