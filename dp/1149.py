# https://www.acmicpc.net/problem/1149
# RGB거리
# DP
import sys
I=sys.stdin.readline
T=int
R=range
G=lambda:[*map(T,I().split())]
n=T(I())
d=[G()]
for _ in R(n-1):
    t=[];p=d[-1]
    d.append([min(c+p[(i+1)%3],c+p[(i+2)%3])for i,c in enumerate(G())])
print(min(d[-1])) 
# 0.5초 readline 활용, 미리 DP 할당하면 시간 초과 우려
# 양 옆의 집의 색상이 일치 안해야한다.
# 각 색상별로 이전까지 최소값이 저장되어 있다고 가정하면서 다음 색상 검색

