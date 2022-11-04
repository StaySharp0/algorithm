# https://www.acmicpc.net/problem/11399
I=sorted(map(int,[*open(0)][1].split()))
print(sum([(len(I)-i)*x for i,x in enumerate(I)]))