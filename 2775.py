# 2
# 1
# 3 - 6  -> 0층 3호 = 1 + 2 + 3
# 2
# 3 - 10 -> 1층 3호 -> 1 + 3 + 6

from itertools import islice

O = {}
for _ in range(int(input())):
  k, n = int(input()), int(input())

  for r in range(k+1):
    for c in range(1, n+1):
      if r in O and c in O[r]:
        continue

      if c == 1:
        O[r] = {}

      if r == 0:
        O[r][c] = c
      else:
        O[r][c] = sum(islice(O[r-1].values(),c))

  print(O[k][n])