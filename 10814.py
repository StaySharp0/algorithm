# https://www.acmicpc.net/problem/10814
# 정렬

print(*[' '.join(_) for _ in sorted([_.split() for _ in [*open(0)][1:]],key=lambda x: int(x[0]))],sep='\n')

# print(*sorted([*open(0)][1:],key=lambda a:int(a.split()[0])),sep='')
# 입력값에 \n 있는걸 활용했다 ㅋㅋㅋㅋ 허