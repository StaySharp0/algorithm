for itr, word in [input().split(' ') for _i in range(int(input()))]:
  for w in word:
    print(w * int(itr), end='')
  print()

# for r,_,*s,_ in[*open(0)][1:]:print(''.join(c*int(r)for c in s))
# open 구문, join + for 방식