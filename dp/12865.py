# https://www.acmicpc.net/problem/12865
# 평범한 배낭
# DP
from collections import defaultdict as D
R=range
I=lambda:map(int,input().split())
n,k=I()
d=D(int);d[0]=0
for _ in R(n):
    w,v=I();t={}
    for x,y in [*d.items()]:
        if x+w<=k and y+v>d[x+w]:t[x+w]=y+v
    d.update(t)
print(max(d.values()))

# d[k]가 아닌 이유는 더 적은 무게의 조합에서 가치가 더 큰 경우가 있을 수 있음 

# 접근 1) 무게가 적은걸로 많이 X / 가장 가치 있는 순으로 X -> 정렬로 해소되지 않음
#         백트랙킹으로 접근 가능하나 DP 문제이므로 DP로 해결해보자
#         결국, 당장 들었을 때 가치와 안들고 갔을 때 미래 가치를 비교해서 최대값을 찾아야함
