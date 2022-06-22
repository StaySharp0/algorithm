O = {}
for u in input():
  O.setdefault(u.upper(), 0)
  O[u.upper()]  += 1

O = sorted(O.items(), key=lambda item: item[1])

if len(O) == 1:
  print(O[0][0])
else:
  print('?' if O[-1][1] == O[-2][1] else O[-1][0])