# https://www.acmicpc.net/problem/11727
# DP
# 9095 문제와 유사, -2인 경우 타일이 2개임

R=[1,1]
for x in range(int(input())+1):
  l=len(R)
  if x>=l:
    for i in range(l, x+1): R.append((R[i-1]+2*R[i-2])%10007)
print(R[-1])

# s=t=1
# for _ in range(int(input())):s,t=t,(2*s+t)%10007
# print(s)