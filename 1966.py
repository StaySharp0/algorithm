# https://www.acmicpc.net/problem/1966

for _ in range(int(input())):
  N,M=map(int, input().split())
  q=[[i,x] for i,x in enumerate(map(int, input().split()))]
  r=0
  while q!=[]:
    a=q.pop(0)
    c=True
    for x in q:
      if a[1]<x[1]:
        q.append(a)
        c=False
        break
    if c:
      r+=1
      if M==a[0]:
        print(r)
        break