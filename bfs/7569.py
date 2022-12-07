# https://www.acmicpc.net/problem/7569
# 토마토
# BFS
import sys
from collections import deque as D
R=range
T=int
M=map
I=sys.stdin.readline
x=[-1,0,1,0,0,0]
y=[0,1,0,-1,0,0]
z=[0,0,0,0,1,-1]
m,n,h=M(T,I().split())
g=[]
p=[]
r=[]
for i in R(h):
    t=[]
    for j in R(n):
        t.append([*M(T,I().split())])
        for k in R(m):
            r.append([i,j,k])
            if t[j][k]==1:p.append([i,j,k])
    g.append(t)
o=0
q=D([p])
while q:
    t=[]
    for l in q.popleft():
        a,b,c=l
        for i in R(6):
            d,e,f=a+x[i],b+y[i],c+z[i]
            if 0<=d<h and 0<=e<n and 0<=f<m and g[d][e][f]==0:t.append([d,e,f]);g[d][e][f]=1
    if t:q.append(t);o+=1
for i in r:
    a,b,c=i
    if g[a][b][c]==0:print(-1);exit()
print(o)
# 적어도 100*100줄 입력이 들어오므로 sys 활용import
# tip: 범위 연산 합칠 수 있음 0<=a<h
