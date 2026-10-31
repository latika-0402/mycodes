# cook your dish here
# cook your dish here
t = int(input())
for _ in range(t):
    a, b, a1, b1, a2, b2 = map(int, input().split())
    required = {a, b}
    lang1 = {a1, b1}
    lang2 = {a2, b2}
    if required.issubset(lang1):
        print(1)
    elif required.issubset(lang2):
        print(2)
    else:
        print(0)