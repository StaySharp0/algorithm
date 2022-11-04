# https://www.acmicpc.net/problem/2630
# 분할정복, 재귀
def R(N,M):
  w,b=0,0
  S=sum(map(sum,M))
  if S==0:return 1,0
  elif S==N*N:return 0,1
  else:
    n=N//2
    for r,c in[(0,0),(0,n),(n,0),(n,n)]:
      x,y=R(n,[p[c:c+n]for p in M[r:r+n]])
      w+=x
      b+=y
  return w,b
I=[[*map(int,x.split())]for x in[*open(0)][1:]]
L=len(I)
print('%d\n%d'%R(L,I))