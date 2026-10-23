# cook your dish here
A,B,C,X=map(int,input().split())
l=[]
l.extend([A,B,C])
if X in l:print("YES")
else:print("NO")