# https://www.acmicpc.net/problem/1992
# 분할정복, 재귀
# 2630 문제랑 유사
def R(N,M):
  S=sum(map(sum,M))
  if S==0:return'0'
  elif S==N*N:return'1'
  else:
    t='('
    n=N//2
    for r,c in[(0,0),(0,n),(n,0),(n,n)]:
      t+=R(n,[p[c:c+n]for p in M[r:r+n]])
    return t+')'
I=[[int(d)for d in x[:-1]]for x in[*open(0)][1:]]
print(R(len(I),I))