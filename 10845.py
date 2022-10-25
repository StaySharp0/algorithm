# https://www.acmicpc.net/problem/10845

q=[]
for x in [x.split() for x in [*open(0)][1:]]:
  c=x[0]
  l=len(q)
  if c == "pop": 
    print(q.pop(0) if l else -1)
  elif c == "size": 
    print(l)
  elif c == "empty":
    print(0 if l else 1)
  elif c == "front":
    print(q[0] if l else -1)
  elif c == "back":
    print(q[-1] if l else -1)
  else:
    q.append(x[1])