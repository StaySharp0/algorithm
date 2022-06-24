import itertools

_,C = map(int, input().split())
temp = 0

for i in itertools.combinations(map(int, input().split()),3):
  if C >= sum(i) and C - sum(i) < C - temp:
    temp = sum(i)

print(temp)

# 무작위대입법을 위한 함수(순서와 상관없는 경우의 수  계산) 
# itertools.combinations 