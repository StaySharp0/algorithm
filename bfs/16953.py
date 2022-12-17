# https://www.acmicpc.net/problem/16953
# A → B
# BFS
from collections import deque as D
a,b=map(int,input().split())
q=D([[a]])
r=1
while q:
    t=[]
    for i in q.popleft():
        if i>b:continue
        if i==b:print(r);exit()
        t.extend([i*2,i*10+1])
    if t:r+=1;q.append(t)
print(-1)
