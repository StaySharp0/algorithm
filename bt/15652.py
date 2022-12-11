# https://www.acmicpc.net/problem/15652
# N과 M (4)
# 백트래킹
n,m=map(int,input().split())
t=[]
def R(s):
    if len(t)==m:print(*t,sep=' ');return
    for i in range(s,n+1):t.append(i);R(i);t.pop()
R(1)
