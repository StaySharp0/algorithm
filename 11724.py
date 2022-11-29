# https://www.acmicpc.net/problem/11724
# 그래프 DFS BFS
from collections import deque as D
T=int
P=map
E=range
I=[*open(0)]
N,M=P(T,I[0].split())
N+=1
G=[[0]*N for _ in E(N)]
V=[1]*N
Q=D()
R=0
for i in I[1:]:
    a,b=P(T,i.split())
    G[a][b]=1
    G[b][a]=1

for i in E(1,N):
    if V[i]:Q.append(i);V[i]=0;R+=1
    while Q:
        v=Q.popleft();V[v]=0
        for j in E(1,N):
            if G[v][j] and V[j]:Q.append(j);V[j]=0
print(R)
