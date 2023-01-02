# https://www.acmicpc.net/problem/2206
# 벽 부수고 이동하기
# BFS
from collections import *
R=range
I=input
M=lambda x:map(int,x)
n,m=M(I().split())
g=[0]*n
for i in R(n):g[i]=[*M(I())]
v=[[[1,1]for _ in R(m)]for _ in R(n)]
x=[-1,0,1,0]
y=[0,1,0,-1]
q=deque([(0,0,1)])
while q:
    i,j,k=q.popleft()
    if i==n-1 and j==m-1:print(v[i][j][k]);exit(0)
    for _ in R(4):
        a=i+x[_];b=j+y[_]
        if 0<=a<n and 0<=b<m:
            if g[a][b]and k:q.append((a,b,0));v[a][b][0]=v[i][j][1]+1
            elif g[a][b]==0 and v[a][b][k]==1:q.append((a,b,k));v[a][b][k]=v[i][j][k]+1
print(-1)

# 벽을 부신경우와 안부신 경우 두가지의 가능성을 탐색해야하는데 한번 부시면 더이상
# 부실 수 있는 경우를 탐색하지 않음
