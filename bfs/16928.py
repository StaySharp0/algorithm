# https://www.acmicpc.net/problem/16928
# 뱀과 사다리 게임
# BFS
from collections import deque as D
R=range
m=[[1,i] for i in R(101)]
for i in [*open(0)][1:]:a,b=map(int,i.split());m[a][1]=b
q=D([[[0,1]]])
s=1
while q:
    t=[]
    for d in q.popleft():
        for i in R(1,7):
            n=d[1]+i
            if n==100:print(d[0]+1);exit()
            if n<100 and m[n][0]:m[n][0]=0;t.append((d[0]+1,m[n][1]))
    q.append(t)
# 주사위 던진 횟수를 그룹으로 BFS 탐색
