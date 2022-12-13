# https://www.acmicpc.net/problem/15666
# N과 M (12)
# 백트랙킹
I=lambda:map(int,input().split())
n,m=I()
a=sorted(I())
t=[]
def D(a):
    if len(t)==m:print(*t);return
    o=[]
    for i,x in enumerate(a):
        if x not in o:t.append(x);D(a[i:]);t.pop();o.append(x)
D(a)
