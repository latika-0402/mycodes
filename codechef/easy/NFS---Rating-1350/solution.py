# cook your dish here
try:
    t_cases = int(input())
except EOFError:
    t_cases = 0

for _ in range(t_cases):
    u, v, a, s = map(int, input().split())

    if u <= v:
        print("Yes")
    else:
        v_squared = (u**2) - (2 * a * s)
        if v_squared <= (v**2):
            print("Yes")
        else:
            print("No")