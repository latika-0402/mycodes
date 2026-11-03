# cook your dish here
# cook your dish here
s = input().strip()

# Dictionary to store the frequency of each consecutive pair
counts = {}

for i in range(len(s) - 1):
  pair = s[i] + s[i + 1]
  if pair in counts:
    counts[pair] += 1
  else:
    counts[pair] = 1

# Count how many pairs appear at least twice
ans = 0
for pair in counts:
  if counts[pair] >= 2:
    ans += 1

print(ans)