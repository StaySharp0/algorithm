# https://www.acmicpc.net/problem/2108
from collections import Counter

n=[*map(int, [*open(0)][1:])]
n.sort()
l=len(n)
m=Counter(n).most_common(2)

print(
  round(sum(n)/l),
  n[l//2],
  m[-1][0] if m[-1][1]==m[0][1] else m[0][0],
  n[-1]-n[0],
  sep='\n')


# from collections import Counter
# n=[*map(int, [*open(0)][1:])]
# n.sort()
# l=len(n)
# m=Counter(n).most_common(2)
# print(round(sum(n)/l),n[l//2],m[-1][0] if m[-1][1]==m[0][1] else m[0][0],n[-1]-n[0],sep='\n')


# tip: 갯수 세기 Counter