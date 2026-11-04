class Solution:    
    def findUnion(self, a, b):
        # code here
        a,b=set(a),set(b)
        c=a|b
        return list(c)