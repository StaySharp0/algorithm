# https://www.acmicpc.net/problem/2805
# 이분탐색
from functools import reduce
_,M=map(int, input().split())
A=[*map(int, input().split())]
R=[]
s=0
e=max(A)
while s<=e:
  m=(e+s)//2
  h=reduce(lambda a,c: a+c-m if c>m else a ,A,0)
  if h>=M:
    s=m+1
    R.append(m)
  elif h<M:e=m-1
print(R[-1])