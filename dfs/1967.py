# https://www.acmicpc.net/problem/1967
# 트리의 지름
# DFS, 1167번 문제랑 같은거처럼 보임
import sys
sys.setrecursionlimit(10**6)
R=range
I=lambda:map(int,input().split())
n,=I()
g=[{} for _ in R(n+1)]
for _ in R(n-1):s,e,w=I();g[s][e]=w;g[e][s]=w
def D(s,t):
    for e,w in g[s].items():
        if t[e]==0:t[e]=t[s]+w;D(e,t)
    return t
T=lambda:{i:0 for i in R(n+1)}
M=lambda x:max(x,key=x.get)
t=D(1,T())
t[1]=0
s=M(t)
t=D(s,T())
t[s]=0
print(t[M(t)])

# 출발점을 0으로 초기화 안해서 제일먼 노드 구하는 부분에서 문제가 있었음
