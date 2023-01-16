# https://www.acmicpc.net/problem/24416
# 알고리즘 수업 - 피보나치 수 1
# DP
f=[0,1,1]+[0]*48
n=int(input())
for i in range(3, n+1):f[i]=f[i-1]+f[i-2]
print(f[n],n-2)
