# https://www.acmicpc.net/problem/11725
# 트리의 부모 찾기
# BFS
import sys
from collections import deque as D
R=range
T=int
I=sys.stdin.readline
n=T(I())+1
g=[[] for _ in R(n)]
for _ in R(n-2):x,y=map(T,I().split());g[x].append(y);g[y].append(x)
v=[0]*n
v[1]=1
q=D([1])
while q:
    p=q.popleft()
    for c in g[p]:
        if v[c]==0:v[c]=p;q.append(c)
print(*v[2:],sep='\n')
# 접근 1) 100,000이면 input으로 힘들 수 있음
#         v를 활용해서 부모 정보를 저장함
# 접근 2) 이차원 배열 사용했다가 메모리 부족 발생
