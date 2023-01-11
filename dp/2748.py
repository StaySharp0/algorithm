# https://www.acmicpc.net/problem/2748
# 피보나치 수 2
# DP
d=[0,1]
n=int(input())
for i in range(2,n+1):d.append(d[i-1]+d[i-2])
print(d[n])
