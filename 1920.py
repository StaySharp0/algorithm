# https://www.acmicpc.net/problem/1920
# 자료구조 이분탐색 해시

I=[*open(0)]
O={}
for k in I[1].split():
  O.setdefault(k,0)

print(*[1 if k in O else 0 for k in I[3].split()],sep="\n")

# z,z,t,t=open(0)
# z={*z.split()}
# for i in t.split():print(+(i in z))

# open을 디스트럴처링
# 제너레이터를 활용한 딕셔너리 초기화 방법
# +True를 통한 단축