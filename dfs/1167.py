# https://www.acmicpc.net/problem/1167
# 트리의 지름
# DFS
import sys
sys.setrecursionlimit(10**6)
R=range
I=lambda:map(int,sys.stdin.readline().split())
v,=I()
g=[{} for _ in R(v)]
for _ in R(v):
    s,*i=[*I()][:-1]
    for j in R(0,len(i),2):g[s-1][i[j]-1]=i[j+1]
def D(s,t):
    for e,d in g[s].items():
        if t[e]==0:t[e]=t[s]+d;D(e,t)
T=lambda:{i:0 for i in R(v)}
M=lambda x:max(x,key=x.get)
t=T()
r=D(0,t)
t[0]=0
s=M(t)
t=T()
D(s,t)
t[s]=0
print(t[M(t)])

# 접근 1) 플로이드-워셜 하기에는 node가 너무 많음
# 접근 2) 도저히 모르겠어서 검색 알고리즘 증명(https://blog.myungwoo.kr/112)
#         1. 한 노드에서 가장 먼 노드 찾기
#         2. 해당 노드에서 가장 먼 노드의 길이가 트리의 지름
