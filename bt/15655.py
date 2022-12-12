# https://www.acmicpc.net/problem/15655
# N과 M (6)
# 백트랙킹
I=lambda:map(int,input().split())
n,m=I()
a=sorted(I())
t=[]
def D(s):
    if len(t)==m:print(*t);return
    for i in range(s,n):
        if a[i] not in t:t.append(a[i]);D(i+1);t.pop()
D(0)
