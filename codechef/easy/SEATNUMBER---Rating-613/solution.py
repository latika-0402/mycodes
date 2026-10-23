# cook your dish here
t=int(input())
for _ in range(t):
    d={1:"Lower Double",2:"Lower Double",3:"Lower Double",4:"Lower Double",5:"Lower Double",6:"Lower Double",7:"Lower Double",8:"Lower Double",9:"Lower Double",
    10:"Lower Double",11:"Lower Single",12:"Lower Single",13:"Lower Single",14:"Lower Single",15:"Lower Single",16:"Upper Double",17:"Upper Double",18:"Upper Double",19:"Upper Double",20:"Upper Double",21:"Upper Double",
    22:"Upper Double",23:"Upper Double",24:"Upper Double",25:"Upper Double",26:"Upper Single",27:"Upper Single",28:"Upper Single",29:"Upper Single",30:"Upper Single"}
    n=int(input())
    for i,j in d.items():
        if i==n:
            print(d[i])