input()
A = list(map(int, input().split()))
print(min(A), max(A))

# print(min(s:=[*map(int,[*open(0)][1].split())]),max(s))
# 결과 중에 변수 저장 가능 min(s:=[1]), max(s)
#[*map()] 을 통해서 리스트 생성