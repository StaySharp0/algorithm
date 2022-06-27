# O = [0] * 10001

# # 메모리 초과 원인처럼 보임
# # for _ in [*open(0)][1:]:
# #   O[int(_)] += 1

# for _ in range(int(input())):
#    O[int(input())] += 1

# for i, _ in enumerate(O):
#   for _ in range(_):
#     print(i)

import sys
input = sys.stdin.readline

O = [0] * 10001

for _ in range(int(input())):
   O[int(input())] += 1

for i, _ in enumerate(O):
  for _ in range(_):
    print(i)

# 입력속도 때문에 시간 제한에 걸린 경우
# import sys
# input = sys.stdin.readline 활용