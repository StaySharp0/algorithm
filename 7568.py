# https://www.acmicpc.net/problem/7568
# 브루트포스
# 버블 소트

O=[]
P=[[*map(int,_.split())] for _ in [*open(0)][1:]]
for b in P:
  w,h=b
  count=1
  for a in P:
    _w,_h=a
    if w < _w and h <_h:
      count+=1
  O.append(count)
print(*O)