# https://www.acmicpc.net/problem/7576
# 그래프, BFS

# 1인 위치를 찾아서 미리 큐에 담고, BFS, 검색범위를 어레이로 묶어서 스텝 계산

from collections import deque as D
def S(s):return map(int,s.split())
E=enumerate
I=[*open(0)]
M,N=S(I[0])
G=[[*S(s)] for s in I[1:]]
Q=D()
T=[]
for i,r in E(G):
    for j,x in E(r):
        if x==1:T.append((i,j))
Q.append(T)
V=[(0,1),(1,0),(0,-1),(-1,0)]
R=-1
while Q:
    T=Q.popleft()
    t=[]
    for y,x in T:
        for i,j in V:
            i+=y;j+=x
            if i<0 or j<0 or i==N or j==M or G[i][j]!=0:continue
            G[i][j]=1
            t.append((i,j))
    if t:Q.append(t)
    R+=1
E=False
for r in G:
    for x in r:
        if x==0:E=True
print(-1 if E else R)
