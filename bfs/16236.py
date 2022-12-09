# https://www.acmicpc.net/problem/16236
# 아기 상어
# BFS
from collections import deque as D
R=range
M=map
T=int
i=[*open(0)]
n=T(i[0])
g=[]
for r in i[1:]:g.append([*M(T,r.split())])
x=[-1,0,1,0]
y=[0,1,0,-1]
for i in R(n):
    for j in R(n):
        if g[i][j]==9:r=i;c=j
def B(r,c,s):
    q=D([[r,c]]);v=[[1]*n for _ in R(n)];v[r][c]=0;d=[[0]*n for _ in R(n)];t=[]
    while q:
        r,c=q.popleft()
        for i in R(4):
           a=r+x[i];b=c+y[i]
           if 0<=a<n and 0<=b<n and v[a][b]and g[a][b]<=s:
               v[a][b]=0;q.append([a,b]);d[a][b]=d[r][c]+1
               if g[a][b]and g[a][b]<s:t.append([-d[a][b],-a,-b])
    return sorted(t)
e=b=0
w=2
while 1:
    t=B(r,c,w)
    if len(t)==0:break
    g[r][c]=0;d,r,c=t.pop();e+=-d;r=-r;c=-c;g[r][c]=0;b+=1
    if b==w:w+=1;b=0
print(e)
