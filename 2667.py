# https://www.acmicpc.net/problem/2667
# DFS, BFS
from collections import deque as D
R=range
E=enumerate
T=int
I=input
n=T(I())
v=[[1]*n for _ in R(n)]
m=[[*map(T,[*I()])]for _ in R(n)]
q=D()
u=[-1,0,1,0]
l=[0,1,0,-1]
r=[]
def C(c,d):return c>=0 and c<n and d>=0 and d<n 
for i in R(n*n):
    a,b=i//n,i%n;e=0
    if m[a][b]and v[a][b]:q.append((a,b));v[a][b]=0
    while q:
        a,b=q.popleft();e+=1
        for i in R(4):
            c=a+u[i];d=b+l[i]
            if C(c,d)and m[c][d]and v[c][d]:q.append((c,d));v[c][d]=0
    if e:r.append(e)
r.sort()
print(len(r),*r,sep='\n')
