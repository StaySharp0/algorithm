# https://www.acmicpc.net/problem/2178
# 그래프, DFS
from collections import deque as q
N,M=map(int,input().split())
G=[]
for _ in range(N):G.append([int(x) for x in input()])
X=[(1,0),(0,-1),(-1,0),(0,1)]
Q=q([(0,0)])
while Q:
    x,y=Q.popleft()
    for a,b in X:
        a=x+a;b=y+b
        if a<0 or b<0 or a==N or b==M or G[a][b]==0:continue
        if G[a][b]==1:G[a][b]=G[x][y]+1;Q.append((a,b))
print(G[-1][-1])

# 지나간 곳은 다시 가지 않도록 코스트 계산
