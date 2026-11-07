# cook your dish here
import sys


def solve():
  input_data = sys.stdin.read().split()
  if not input_data:
    return

  t = int(input_data[0])
  idx = 1

  for _ in range(t):
    x = int(input_data[idx])
    s = input_data[idx + 1]
    idx += 2

    carlsen_points = 0
    chef_points = 0

    for char in s:
      if char == "C":
        carlsen_points += 2
      elif char == "N":
        chef_points += 2
      elif char == "D":
        carlsen_points += 1
        chef_points += 1

    if carlsen_points > chef_points:
      print(60 * x)
    elif chef_points > carlsen_points:
      print(40 * x)
    else:
      # Tie: Carlsen is the defending champion and wins even if tied
      print(55 * x)


if __name__ == "__main__":
  solve()