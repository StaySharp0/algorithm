try:
  while 1:
    print(sum(map(int,input().split())))
except:
  exit()

# 입력갯수를 모르면 예외처리
# for a,_,b,_ in open(0):print(int(a)+int(b))