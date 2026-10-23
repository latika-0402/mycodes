# cook your dish here
t = int(input())
for _ in range(t):
    A,B,C = map(int,input().split())
    if max(A, C) <= B:
        print("Yes")
    else:
        print("No")