# https://www.acmicpc.net/problem/1929
# 소수탐색

# N,M=map(int,input().split())
# a=[2]
# for x in range(3,M+1):
#   n=True
#   for y in a:
#     if x%y==0:
#       n=False
#       break
#   if n: a.append(x)
# for x in a:
#   if x>=N:print(x)

# 에라토스테네스의 체
# 1. 구하려는 소수 범위를 미리 설정
# 2. 2부터 배수 제거

N,M=map(int,input().split())
r=[x for x in range(0,M+1)]
r[1]=0
for x in range(2,M+1):
  y=2
  while x*y<=M:
    r[x*y]=0
    y+=1
for x in r:
  if x>=N:print(x)
