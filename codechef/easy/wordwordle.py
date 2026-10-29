t=int(input())
for _ in range(t):
    s=input()
    t=input()
    result=[]
    for i in range(len(s)):
        if s[i]==t[i]:
            result.append("G")
        else:result.append("B")
    print("".join(result))