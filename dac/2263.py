# https://www.acmicpc.net/problem/2263
# 트리의 순회
# divde and conquer
import sys
sys.setrecursionlimit(10**6)
I=lambda:[*map(int,sys.stdin.readline().split())]
n,=I()
i=I()
p=I()
x={v:_ for _,v in enumerate(i)}
def D(a,b,c,d):
    if a>=b or c>=d:return
    print(p[d-1],end=" ");y=x[p[d-1]];z=c+y-a;D(a,y,c,z);D(y+1,b,z,d-1)
D(0,n,0,n)

# 인오더는 중간을 기점으로 왼쪽서브트리->루트->오른쪽서브트리
# 포스트 오더는 왼쪽서브트리->오른쪽서브트리->루트
# 접근 1) 배열 슬라이싱 활용했더니 18%에서 메모리 초과
# 접근 2) index 사용했더니 시간 초과 
# 접근 3) 슬라이싱으로 조건 검사했더니 시간 초과
