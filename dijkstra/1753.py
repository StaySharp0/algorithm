# https://www.acmicpc.net/problem/1753
# 최단경로
# dijstra
import sys as S,heapq as H
M=S.maxsize
R=range
I=lambda:map(int,S.stdin.readline().split())
v,e=I()
k,=I()
g=[[]for _ in R(v+1)]
for _ in R(e):s,e,w=I();g[s].append([e,w])
def D(s):
    q=[];d=[M]*(v+1);H.heappush(q,(0,s));d[s]=0
    while q:
        c,s=H.heappop(q)
        for e,w in g[s]:
            x=c+w
            if d[e]>x:d[e]=x;H.heappush(q,(x,e))
    return [x if x<M else 'INF'for x in d][1:]
print(*D(k),sep='\n')

# 일반적인 다익스트라 문제?
# '서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.' 놓친 포인트

