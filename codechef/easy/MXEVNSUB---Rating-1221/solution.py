# cook your dish here
try:
    t_cases = int(input())
except EOFError:
    t_cases = 0

for _ in range(t_cases):
    n = int(input())

    total_sum = n * (n + 1) // 2
    if total_sum % 2 == 0:
        print(n)
    else:
        print(n - 1)