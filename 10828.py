# https://www.acmicpc.net/problem/10828
# 자료구조, 스택

s=[]
for x in [x.split() for x in [*open(0)][1:]]:
  c=x[0]
  l=len(s)
  if c == "pop": 
    print(s.pop() if l else -1)
  elif c == "size": 
    print(l)
  elif c == "empty":
    print(0 if l else 1)
  elif c == "top":
    print(s[-1] if l else -1)
  else:
    s.append(x[1])

# 숏코딩
# 배열 비었는지 검사 팁: s==[] 

