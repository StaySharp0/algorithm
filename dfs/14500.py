# https://www.acmicpc.net/problem/14500
# 테트로미노
# DFS
import sys
R=range
T=int
M=map
X=max
I=sys.stdin.readline
n,m=M(T,I().split())
g=[[*M(T,I().split())]for _ in R(n)]
v=[[1]*m for _ in R(n)]
x=[-1,0,1,0]
y=[0,1,0,-1]
t=0
b=X(M(X,g))
def D(i,j,c,s):
    global t,b
    if s+b*(4-c)<t:return
    if c==4:t=X(t,s);return
    for _ in R(4):
        k=i+x[_];l=j+y[_]
        if 0<=k<n and 0<=l<m and v[k][l]:
            if c==2:v[k][l]=0;D(i,j,c+1,s+g[k][l]);v[k][l]=1
            v[k][l]=0;D(k,l,c+1,s+g[k][l]);v[k][l]=1
for r in R(n):
   for c in R(m):
       v[r][c]=0;D(r,c,1,g[r][c]);v[r][c]=1 
print(t)

# 접근 1) 각 좌표점에서 놓을 수 있는 테트로미놈을 놓고 최대값 계산 
#         테트로미놈 형태 좌표값 배열을 만들 수 있는데 19종류라서 너무 복잡함
# 접근 2) 왠만하면 BFS로 하고 싶지만 코드가 복잡해지므로 DFS로 4칸 이동해서 테트로미놈 만드는 방식으로 접근
# 접근 3) 예제 3번째 실패, ㅗ모양이 안만들어져서 그런듯... 
#         2칸 선택해서 - 모양이 됬을때 이동할 다음 칸부터가 아니라 다시 시작지점에서 2칸 찾으면 ㅗ모양 만들 수 있음 
# 접근 4) 시간초과 -> 제일 큰값으로 남은 이동횟수 해도 지금 찾은 값보다 작은 경우는 탐색 안하도록 가지치기
