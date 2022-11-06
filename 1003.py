# https://www.acmicpc.net/problem/1003
# DP
R=[[1,0],[0,1]]
for x in [*open(0)][1:]:
  l=len(R)
  x=int(x)
  for y in range(l,x+1):
    a,b=R[y-1],R[y-2]
    R.append([a[0]+b[0],a[1]+b[1]])
  print('%d %d'%(R[x][0],R[x][1]))

# tip: 배열 홀,짝수 인덱스 출력: [::2],[1::2]