# https://www.acmicpc.net/problem/1697
# BFS
from collections import deque as q
N,K=map(int,input().split())
Q=q([N])
M=10**5+1
D=[M]*M
D[N]=0
while N!=K:
    N=Q.popleft()
    for i in[N-1,N+1,N*2]:
        if i>=0 and i<M:
            if D[i]==M:Q.append(i)
            D[i]=min(D[i],D[N]+1)
print(D[K])

# BFS에서 인덱스 고려 조금더 철저히 해야할 듯
