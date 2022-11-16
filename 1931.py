# https://www.acmicpc.net/problem/1931
# 그리디
# 많은 회의를 할려면? 시작이 빠르고, 회의 시간이 짧은 순 으로 정렬해서 순서대로 보면됨
I=[[*map(int,i.split())]for i in[*open(0)][1:]]
I.sort(key=lambda i:i[0])
I.sort(key=lambda i:i[1])
R=1
E=I[0][1]
for s,e in I[1:]:
    if s>=E:R+=1;E=e
print(R)
