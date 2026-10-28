# cook your dish here
n=input()
n=n.split()
result=[]
for i in range(len(n)):
    if i%2==0:
        result.append(n[i])
print("".join(result))