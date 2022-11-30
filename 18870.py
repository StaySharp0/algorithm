# https://www.acmicpc.net/problem/18870
T=int
I=input
N=T(I())
X=[*map(T,I().split())]
D={v[0]:i for i,v in enumerate(sorted({x:1 for x in X}.items()))}
print(*[D[x] for x in X])
