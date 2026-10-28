# cook your dish here
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input()
    alarms=0
    i=0
    while i<n:
        if s[i]=='1':
            p=min(n,(i+1)+k)
            alarms+=1
            i=p
        else:i+=1
    print(alarms)