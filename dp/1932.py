# https://www.acmicpc.net/problem/1932
# 정수 삼각형
# DP
R=range
T=int
I=input
n=T(I())
d=[[T(I())]]
for i in R(n-1):
    t=[*map(T,I().split())];p=d[i]
    for j in R(i+2):t[j]+=d[i][0]if j==0 else d[i][-1] if j==i+1 else max(d[i][j-1],d[i][j])
    d.append(t)
print(max(d[-1]))
