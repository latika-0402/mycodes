# cook your dish here
t=int(input())
for _ in range(t):
    A,B,C=map(int,input().split())
    print(max(A,B,C))