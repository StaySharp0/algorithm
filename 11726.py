# https://www.acmicpc.net/problem/11726
# DP (11727과 유사)
R=[0,1,2]
N=int(input())
for i in range(3,N+1):R.append(R[i-1]+R[i-2])
print(R[N]%10007)
