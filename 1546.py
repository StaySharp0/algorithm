C = int(input())
E = list(map(int, input().split(' ')))
print( sum([e / max(E) * 100 for e in E]) / C)