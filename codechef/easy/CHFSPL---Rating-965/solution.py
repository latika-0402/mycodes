# cook your dish here
# cook your dish here
t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    total = a + b + c
    min_spell = min(a, b, c)
    
    print(total - min_spell)