Y = int(input())
print(1 if (Y % 4 == 0 and Y % 100 != 0) or Y % 400 == 0 else 0)

# y=int(input())
# print(+((y%100or y//100)%4<1))
# 조건 자체를 다른 연산으로 개선