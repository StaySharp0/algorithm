for i in range(N:=int(input())):
  if N == int(i) + sum([int(i) for i in str(i)]):
    print(i)
    exit()
print(0)

# n=int(input())
# print([*[i for i in range(n)if n==i+sum(map(int,str(i)))],0][0])
# 다구한다음 처음꺼만 사용