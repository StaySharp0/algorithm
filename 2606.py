# https://www.acmicpc.net/problem/2606
# 그래프, BFS, DFS

# BFS로 접근
from collections import deque as q
T=int
I=[*open(0)]
N=T(I[0])+1
M=[[0]*N for _ in range(N)]
for s in I[2:]:a,b=map(T,s.split());M[a][b]=1;M[b][a]=1
Q=q([1])
V=[0]*N
while len(Q):
    v=Q.popleft()
    V[v]=1
    for i,s in enumerate(M[v]):
        if s and V[i]==0:Q.append(i)
print(sum(V)-1)

# 숏코딩
# _,_,*i=open(0)
# for _ in(n:=[-1,1]+[0]*99):
#  for l in i:a,b=map(int,l.split());n[b]=n[a]=n[a]|n[b]
# print(sum(n))

# DFS 풀이 
# n=int(input())+1
# c=[[]for i in range(n)]
# v=[0]*n
# for e in range(int(input())):
#     a,b=list(map(int,input().split()))
#     c[a]+=[b]
#     c[b]+=[a]
# def d(n):
#     if v[n]==0:
#         v[n]=1
#         for m in c[n]:
#             d(m)
# d(1)
# print(sum(v[2:]))
