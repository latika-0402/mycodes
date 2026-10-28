# cook your dish here
t=int(input())
for _ in range(t):
    a,b,c,d,e,f=map(int,input().split())
    alice=a+b+c-min(a,b,c)
    bob=d+e+f-min(d,e,f)
    if alice>bob:print("Alice")
    elif alice<bob:print("Bob")
    else:print("Tie")