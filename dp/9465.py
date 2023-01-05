# https://www.acmicpc.net/problem/9465
# 스티커
# DP
R=range
I=input
T=int
X=max
for i in R(T(I())):
    n=T(I());s=[[*map(T,I().split())]for _ in R(2)]
    if n>1:
        s[0][1]+=s[1][0];s[1][1]+=s[0][0]
        for j in R(2,n):s[0][j]+=X(s[1][j-1],s[1][j-2]);s[1][j]+=X(s[0][j-1],s[0][j-2])
    print(X(s[0][n-1],s[1][n-1]))

# 대각선으로 이동, 한칸이 아닌 한칸이상의 대각선 방향으로 갈 수 있음 
