# https://www.acmicpc.net/problem/15650
# N과 M (2)
# 백트랙킹, DFS
n,m=map(int,input().split())
t=[]
def D(s):
    if len(t)==m:print(*t,sep=' ');return
    for i in range(s,n+1):
        if i not in t:t.append(i);D(i+1);t.pop()
D(1)
# 접근 1) O(n*m) 순회 set을 활용한 중복 제거
# 접근 2) DFS 하면서 이전에 출력했던 수가 있으면 넘기고 탐색
