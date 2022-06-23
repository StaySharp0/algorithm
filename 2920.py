if (s:=[*open(0)][0][::2]) == '12345678':
  print('ascending')
elif s == '87654321':
  print('descending')
else:
  print('mixed')

# print({"2345678":"ascending","7654321":"descending"}.get(input()[2::2],"mixed"))
# 접근은 비슷 첫번째 숫자는 중요하지 않기 때문에 생략