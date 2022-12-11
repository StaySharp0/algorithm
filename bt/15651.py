# https://www.acmicpc.net/problem/15651
# N과 M (3)
# 백트랙킹
n,m=map(int,input().split())
t=[]
def R():
    if len(t)==m:print(*t);return
    for i in range(1,n+1):t.append(i);R();t.pop()
R()
