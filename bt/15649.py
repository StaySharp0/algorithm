# https://www.acmicpc.net/problem/15649
# N과 M (1)
# 백트랙킹
n,m=map(int,input().split())
t=[]
def D():
    if len(t)==m:print(*t,sep=' ');return
    for i in range(1,n+1):
        if i not in t:t.append(i);D();t.pop()
D()
# 접근 1) 이중포문으로 해결가능 하지만 백트래킹 연습을 위해서 백트래킹으로 풀이
