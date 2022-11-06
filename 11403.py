# https://www.acmicpc.net/problem/11403
# 그래프, 플루이드-워셜

M=[x.split()for x in [*open(0)][1:]]
N=len(M)
for k in range(N):
  for a in range(N):
    for b in range(N):
      if M[a][k]!='0' and M[k][b]!='0':M[a][b]='1'
for x in M:print(' '.join(x))