N = int(input())
for i in range(1, 10):
  print('%d * %d = %d' % (N, i, N * i))

# a=b=int(input());exec("print(a,'*',b//a,'=',b);b+=a;"*9)
# exec 문법 신기