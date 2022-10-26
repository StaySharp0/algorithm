# https://www.acmicpc.net/problem/1654
# 이분 탐색
import sys
sys.setrecursionlimit(10**6)

I=[*open(0)]
N,K=map(int,I[0].split(' '))
I=[*map(int,I[1:])]
R=0
s=1
e=max(I)
while s<=e:
  m=(s+e)//2
  k=sum(map(lambda x:x//m,I))
  if k<K:e=m-1
  else:s=m+1
print(e)
