# cook your dish here
import sys


def solve():
  s = sys.stdin.readline().strip()
  if not s:
    return
  freq = {}
  for char in s:
    if char.isalpha():
      lower_char = char.lower()
      freq[lower_char] = freq.get(lower_char, 0) + 1

  if not freq:
    return
  best_char = min(freq.keys(), key=lambda c: (-freq[c], c))

  print(best_char)


if __name__ == "__main__":
  solve()