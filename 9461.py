# https://www.acmicpc.net/problem/9461
# 파도반 수열
# DP
m=[0,1,1,1]+[0]*100
for i in [*open(0)][1:]:
    n=int(i)
    for i in range(1,n-2):m[i+3]=m[i]+m[i+1]
    print(m[n])
