# cook your dish here
t=int(input())
for _ in range(t):
    d,s,e=map(int,input().split())
    if s<=d<=e:
        print("Take second dose now")
    elif e<d:
        print("Too Late")
    else:
        print("Too Early")