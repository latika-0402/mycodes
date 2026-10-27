# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    score_ab = (500 - 2 * x) + (1000 - 4 * (x + y))
    score_ba = (1000 - 4 * y) + (500 - 2 * (y + x))
    print(max(score_ab, score_ba))