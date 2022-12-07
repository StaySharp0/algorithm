# https://www.acmicpc.net/problem/17626
# Four Squares
# DP
T=int
R=range
n=T(input())
r=[0,1]
for i in R(2,n+1):
    m=4
    for j in R(1,T(i**0.5)+1):m=min(m,r[i-j**2])
    r.append(m+1)
print(r[n])

# 각 숫자를 만들기 위한 최소 제곱수가 미리 구해졌다고 가정
