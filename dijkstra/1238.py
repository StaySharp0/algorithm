# https://www.acmicpc.net/problem/1238
# 파티
# 다익스트라
from collections import *
import heapq as H, sys
R=range
I=lambda:map(int,sys.stdin.readline().split())
g=defaultdict(dict)
n,m,x=I();n+=1
for _ in R(m):s,e,t=I();g[s][e]=t
def D(s):
    q=[];d=[1e6]*n;H.heappush(q,(0,s));d[0]=0;d[s]=0
    while q:
        c,s=H.heappop(q)
        if d[s]<c:continue
        for e,t in g[s].items():
            x=c+t
            if d[e]>x:d[e]=x;H.heappush(q,(x,e))
    return d
r=D(x)
for i in R(1,n):r[i]+=D(i)[x]
print(max(r))

# 접근 1) X를 제외한 도시 -> X  시간 +  X -> 도시 복귀 시간 중 최대값 찾기 
#         최대 시간: 100*1000이므로 대충 1e6
