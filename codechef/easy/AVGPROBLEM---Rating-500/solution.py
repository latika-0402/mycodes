# cook your dish here
t=int(input())
for _ in range(t):
    A,B,C=map(int,input().split())
    if (A+B)/2>C:
        print("YES")
    else:print('NO')