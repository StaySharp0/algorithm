# https://www.acmicpc.net/problem/15654
# N과 M (5)
# 백트랙킹
I=lambda:map(int,input().split())
n,m=I()
a=sorted(I())
t=[]
def D():
    if len(t)==m:print(*t);return
    for i in a:
        if i not in t:t.append(i);D();t.pop()
D()
