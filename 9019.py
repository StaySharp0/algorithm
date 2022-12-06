# https://www.acmicpc.net/problem/9019
# DSLR
# 그래프, BFS

# 모든 경우의 수 탐색
from collections import deque as D
import sys
T=int
I=sys.stdin.readline
for i in range(T(I())):
    s,e=map(T,I().split());q=D();v=[1]*10000;q.append(('',s))
    while q:
        c,s=q.popleft() 
        v[s]=0
        if s==e:print(c);break
        t=(s*2)%10000
        if v[t]:q.append((c+'D',t));v[t]=0
        t=(s-1)%10000
        if v[t]:q.append((c+'S',t));v[t]=0
        t=(s*10+(s//1000))%10000
        if v[t]:q.append((c+'L',t));v[t]=0
        t=(s//10+(s%10)*1000)%10000
        if v[t]:q.append((c+'R',t));v[t]=0
