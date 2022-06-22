print('%d\n%d' % max([(int(input()), i) for i in range(1,10)], key=lambda x: x[0]))

# point
# n개 행 입력 방법 처리
# print(*max((int(input()),i+1)for i in range(9)))