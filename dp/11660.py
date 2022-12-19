# https://www.acmicpc.net/problem/11660
# 구간 합 구하기 5
# DP
import sys
I=lambda:map(int,sys.stdin.readline().split())
R=range
n,m=I()
d=[[0]*(n+1) for _ in R(n+1)]
for i in R(1,n+1):
    for j,v in enumerate(I()):j+=1;d[i][j]=d[i-1][j]+d[i][j-1]-d[i-1][j-1]+v
for _ in R(m):i,j,k,l=I();print(d[k][l]-d[k][j-1]-d[i-1][l]+d[i-1][j-1])
# 접근 1) 1차원 배열 -> 2차원 배열 X: 2 2 3 4 가 27인 이유는 3 1 은 포함이 되지 않음 사각형 범위
# 접근 2) 제일 큰 누적합 빼기 - 왼쪽사각형 - 아래쪽사각형 + 겹치는 사각형 
