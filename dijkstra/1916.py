# https://www.acmicpc.net/problem/1916
# 최소비용 구하기
# dijkstra
import sys as S,heapq as H
R=range
I=lambda:map(int,S.stdin.readline().split())
n,=I()
m,=I()
g=[[]for _ in R(n+1)]
for _ in R(m):s,e,t=I();g[s].append([e,t])
def D(s):
    q=[];d=[S.maxsize]*(n+1);H.heappush(q,(0,s));d[s]=0
    while q:
        c,s=H.heappop(q)
        if d[s]<c:continue
        for e,w in g[s]:
            x=c+w
            if d[e]>x:d[e]=x;H.heappush(q,(x,e))
    return d 
s,e=I()
print(D(s)[e])

# 일반적인 다익스트라 문제 ?
# 설명은 없지만 중복 경로가 있다고 질문 게시판에 올라와 있음
# 중복 경로 제거를 위해 다음 시작지점까지 최소 비용과 현재 비용을 비교해서
# 현재 비용이 큰 경우 스킵하도록 조건 추가
