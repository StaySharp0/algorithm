# https://www.acmicpc.net/problem/2164 
# 자료구조 큐

from collections import deque
N=deque([*range(1,int(*open(0))+1)])
while len(N) != 1:
  N.popleft()
  if len(N) != 1:N.append(N.popleft())
print(N[0])

# list는 pop(0)은 O(n)이라 느림