# https://www.acmicpc.net/problem/18111
# 최대 높이, 최소 높이 구간의 소요 시간 구해서 최소 시간 경의 출력
I=[*open(0)]
N,M,B=map(int,I[0].split())
I=sum([[*map(int,x.split())]for x in I[1:]], [])
x,y=float('inf'),0
for h in range(min(I),max(I)+1):
  s,i=0,B
  for l in I:
    t=abs(l-h)
    if l>h:
      s+=2*t
      i+=t
    elif l<h:
      s+=t
      i-=t
  if i>=0 and s<=x:
    x,y=s,h
print(x,y,sep=' ')

# tip: 2차원 배열을 1차원 배열로 sum(list, [])