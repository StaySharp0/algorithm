# https://www.acmicpc.net/problem/10026
# 적록색약
# DFS
from collections import deque as D
R=range
T=int
I=input
n=T(I())
m=[]
v=[[1]*n for _ in R(n)]
u=[-1,0,1,0]
l=[0,1,-0,-1]
for i in R(n):m.append([*I()])
k=0
def A(r,c):
    global k;o=m[r][c];v[r][c]=0;q=D();q.append((r,c))
    while q:
        r,c=q.popleft()
        for i in R(4):
            x=r+u[i];y=c+l[i]
            if x>=0 and x<n and y>=0 and y<n and v[x][y] and m[x][y]==o:v[x][y]=0;q.append((x,y)) 
    k+=1
for i in R(n*n):
    r,c=i//n,i%n
    if v[r][c]:A(r,c)
o=k
v=[[1]*n for _ in R(n)]
for i in R(n*n):
    r,c=i//n,i%n
    if m[r][c]=='R':m[r][c]='G'
k=0
for i in R(n*n):
    r,c=i//n,i%n
    if v[r][c]:A(r,c)
print(o,k)
