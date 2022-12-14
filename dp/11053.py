# https://www.acmicpc.net/problem/11053
# 가장 긴 증가하는 부분 수열(LIS)
# DP
I=input
T=int
R=range
n=T(I())
a=[*map(T,I().split())]
d=[1]*n
for i in R(n):
    for j in R(i):
        if a[i]>a[j]:d[i]=max(d[i],d[j]+1)
print(max(d))
