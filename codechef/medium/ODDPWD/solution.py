# cook your dish here
n=input()
result=[]
for i in range(len(n)):
    if i%2==0:
        result.append(n[i])
print("".join(result))