# https://www.acmicpc.net/problem/11651
# 정렬


# print(sorted([[*map(int, _.split())] for _ in [*open(0)][1:]],key=lambda x: x[::-1]),sep='')

for _ in sorted([[*map(int, _.split())][::-1] for _ in [*open(0)][1:]]):print(*_[::-1])