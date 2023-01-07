# https://www.acmicpc.net/problem/2738
# 행렬 덧셈
R=range
I=lambda:map(int,input().split())
n,m=I()
a=[[*I()]for _ in R(n)]
b=[[*I()]for _ in R(n)]
for r in R(n):
    for c in R(m):print(a[r][c]+b[r][c],end=' ')
    print()
