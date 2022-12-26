# https://www.acmicpc.net/problem/1865
# 웜홀
# bellman-ford
import sys as S
R=range
M=S.maxsize
I=lambda:map(int,S.stdin.readline().split())
def B(v,e):
    d=[M]*(v+1);d[1]=0
    for i in R(v):
        for a,b,t in e:
            if d[a]+t<d[b]:
                if i==v-1:return 0
                d[b]=d[a]+t
    return 1
for _ in R(int(input())):
    n,m,w=I();x=[]
    for i in R(m+w):s,e,t=I();x+=[[s,e,t],[e,s,t]]if i<m else [[s,e,-t]]
    print('YNEOS'[B(n,x)::2])

# 도로는 양수 가중치 / 웜홀은 음수 가중치 -> 벨만 포드 알고리즘 사용(복습 필요, 익숙치 않음)
# 시간이 줄어들면서 출발 위치로 돌아올 수 있는지 여부 체크이므로 음의 순환이 발생하는지만 확인하면 됨
# 최단 거리 구하는 문제가 아니므로, d[a]!=M 조건을 제거해야만 통과
