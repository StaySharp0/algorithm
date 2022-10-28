# https://www.acmicpc.net/problem/1874

N=[*map(int, [*open(0)][1:])]
t=[False]
a=[]
n=len(N)
i=0
for x in range(1, n+2):
  while t[-1] == N[i]:
    t.pop()
    a.append('-')
    i+=1
    if i==n: break
  if x <= n:
    t.append(x)
    a.append('+')
if len(t)==1:print('\n'.join(a))
else:print('NO')