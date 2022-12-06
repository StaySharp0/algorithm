# https://www.acmicpc.net/problem/11047
# 동전 0
# 그리디
T=int
M=map
i=[*open(0)]
n,k=M(T,i[0].split())
c=[*M(T,i[1:])]
c.reverse()
r=0
for v in c:
    t=k//v
    if t:r+=t;k-=t*v
print(r)

# 큰 동전부터 확인
