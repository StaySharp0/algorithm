# https://www.acmicpc.net/problem/11650
# 정렬

print(*sorted([*open(0)][1:],key=lambda x: (int(x.split()[0]), int(x.split()[1]))),sep='')

# for i in sorted([[*map(int,s.split())]for s in open(0)][1:]):print(*i)
# 차순위 정렬 가능 -> (),[] 딕셔너리 순서