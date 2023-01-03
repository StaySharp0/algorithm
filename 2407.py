# https://www.acmicpc.net/problem/2407
# 조합
from functools import *
n,m=map(int,input().split())
C=lambda x,y,z=-1:reduce(lambda a,b:a*b,range(x,y,z),1)
print(C(n,n-m)//C(1,m+1,1))
