# https://www.acmicpc.net/problem/11659
# 구간 합 구하기 4
import sys
T=int
M=map
I=sys.stdin.readline
n,m=M(T,I().split())
r=[0]*(n+1)
for i,v in enumerate([*M(T,I().split())]):r[i+1]=r[i]+v
for _ in range(m):s,e=M(T,I().split());print(r[e]-r[s-1])

# 접근: 누적합 선계산, 시작지점 아래 빼기
# ?: 데이터 사이즈가 어느 정도여야지sys.stdin.readline를 써야하는지 의문

# tip: lambda를 활용한 숏코딩
# q=lambda:map(int,input().split())
# n,k=q() 
