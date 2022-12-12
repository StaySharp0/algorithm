# https://www.acmicpc.net/problem/15657
# N과 M (8)
# 백트랙킹
I=lambda:map(int,input().split())
n,m=I()
a=sorted(I())
t=[]
def D(s):
    if len(t)==m:print(*t);return
    for i in range(s,n):t.append(a[i]);D(i);t.pop()
D(0)
