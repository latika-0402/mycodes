# cook your dish here
n = int(input())
max_lead = 0
winner = 0
p1_cumulative = 0
p2_cumulative = 0

for _ in range(n):
    s, t = map(int, input().split())
    p1_cumulative += s
    p2_cumulative += t
    if p1_cumulative > p2_cumulative:
        current_lead = p1_cumulative - p2_cumulative
        current_leader = 1
    else:
        current_lead = p2_cumulative - p1_cumulative
        current_leader = 2
    if current_lead > max_lead:
        max_lead = current_lead
        winner = current_leader

print(winner, max_lead)