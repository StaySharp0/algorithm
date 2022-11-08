# https://www.acmicpc.net/problem/11286
# 우선순위 큐(https://www.daleseo.com/python-heapq)
import heapq as H
h=[]
for I in map(int,[*open(0)][1:]):
    if I!=0:H.heappush(h,[abs(I), I])
    else:print(H.heappop(h)[1] if len(h) else 0)
