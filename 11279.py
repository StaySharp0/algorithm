# https://www.acmicpc.net/problem/11279
# 우선순위 큐(최대힙)
import heapq as H
q=[]
for I in map(int,[*open(0)][1:]):
    if I:H.heappush(q,[-I,I])
    else:print(H.heappop(q)[1]if q!=[]else 0)

#  우선순위 큐 숏코딩 tip:  from heapq import*
