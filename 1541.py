# https://www.acmicpc.net/problem/1541
R=0
for i,s in enumerate(input().split('-')):
    R-=sum([int(n) for n in s.split('+')])*(-1 if i==0 else 1)
print(R)

# - 부터 다음 - 까지 괄호 치면 되어 보임 

a,*b=[sum(map(int,t.split('+'))) for t in input().split('-')]
print(a-sum(b))
# tip: for문 첫번째만 따로 처리하고 싶을 때 unpacking 활용
