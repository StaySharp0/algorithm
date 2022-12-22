# https://www.acmicpc.net/problem/1504
# 특정한 최단 경로
# dijkstra
from collections import *
import sys,heapq as H
R=range
I=lambda:map(int,sys.stdin.readline().split())
n,e=I()
g=defaultdict(dict)
for _ in R(e):a,b,c=I();g[a][b]=c;g[b][a]=c 
x,y=I()
def D(s):
    q=[];d=[1e10]*(n+1);H.heappush(q,(0,s));d[s]=0
    while q:
        c,s=H.heappop(q)
        for e,t in g[s].items():
            x=c+t
            if d[e]>x:d[e]=x;H.heappush(q,(x,e))
    return d
i=D(1)
j=D(x)
k=D(y)
r=min(i[x]+j[y]+k[n],i[y]+k[x]+j[n])
print(r if r<1e10 else -1)

# 1 -> v1 -> v2 -> n, 1 -> v2 -> v1 -> n 경우의 수 2가지 중 최솟값 선택
# INF 계산이 잘못됨 정점을 거쳐가는 일이 발생하므로최악의 경우 1e6을 넘을 수 있다.
# tip: INF 값 대신 sys.maxsize 활용
