# https://www.acmicpc.net/problem/1463
# DP

N,R=int(input()),{1:0,2:1,3:1}
for x in range(4,N+1):
    R[x]=R[x-1]+1
    for a in [3,2]:
        if x%a==0:R[x]=min(R[x],R[x//a]+1)
print(R[N])

# 2와 3과 동시에 나눠질 수 있는 경우
