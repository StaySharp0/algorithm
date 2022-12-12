# https://www.acmicpc.net/problem/15663
# N과 M (9)
# 백트랙킹
I=lambda:map(int,input().split())
n,m=I()
a=sorted(I())
t=[]
def D(a):
    if len(t)==m:print(*t);return
    o=[]
    for i in range(len(a)):
        if a[i]not in o:t.append(a[i]);D(a[:i]+a[i+1:]);t.pop();o.append(a[i])
D(a)
