# cook your dish here
t=int(input())
for _ in range(t):
    l={"A":"T","T":"A","C":"G","G":"C"}
    n=int(input())
    s=input()
    result=""
    for i in s:
        if i in l:
            result+=l[i]
    print(result)