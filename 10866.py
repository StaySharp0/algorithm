# https://www.acmicpc.net/problem/10866

d=[]
for x in [x.split() for x in [*open(0)][1:]]:
  c=x[0]
  l=len(d)
  if c == "size": 
    print(l)
  elif c == "empty":
    print(0 if l else 1)
  elif c == "front":
    print(d[0] if l else -1)
  elif c == "back":
    print(d[-1] if l else -1)
  elif c == "pop_front": 
    print(d.pop(0) if l else -1)
  elif c == "pop_back": 
    print(d.pop() if l else -1)
  elif c == "push_back":
    d.append(x[1])
  else:
    d.insert(0, x[1])