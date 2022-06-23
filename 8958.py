for _ in range(int(input())):
  S = 0
  C = 0
  for i in input():
    if i == 'O':
      C += 1
      S += C
    else:
      C = 0
  print(S)

# for i in[*open(0)][1:]:n=0;print(sum((n:=(n+1)*(j=='O'))for j in i))
