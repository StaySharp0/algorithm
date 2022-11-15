# https://www.acmicpc.net/problem/1927
# 우선순위 큐(최소 힙)
import heapq as H
q=[]
for I in map(int,[*open(0)][1:]):
    if I:H.heappush(q,I)
    else:print(H.heappop(q)if q!=[]else 0)
