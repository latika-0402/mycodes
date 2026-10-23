# cook your dish here
t=int(input())
for _ in range(t):
    N,X,Y=map(int,input().split()) #problems,score,required
    if Y % X == 0 and (Y // X) <= N:
        print("YES")
    else:
        print("NO")
    