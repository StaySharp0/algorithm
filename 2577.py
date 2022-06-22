from functools import reduce

O = {}
for i in str(reduce(lambda x, y: x*y, [int(input()) for i in range(1,4)])):
  O.setdefault(int(i), 0)
  O[int(i)] += 1

for i in range(10):
  print(O[i] if i in O else 0)

# point
# 1157번 문제랑 저장 방식 비슷
# exec('n,m=0,1'+'*int(input())'*3+';print(str(m).count(str(n)));n+=1'*10)