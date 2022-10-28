# https://www.acmicpc.net/problem/10773

r=[]
for x in map(int,[*open(0)][1:]):
  if x:r.append(x)
  else:r.pop()
print(sum(r))