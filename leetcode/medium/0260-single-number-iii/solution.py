class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        l={}
        result=[]
        for i in nums:
            l[i]=l.get(i,0)+1
        for i,j in l.items():
            if j==1:
                result.append(i)
        return result


        