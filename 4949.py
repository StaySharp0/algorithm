# https://www.acmicpc.net/problem/4949

for l in [*open(0)][:-1]:
  s=[]
  try:
    for u in l:
      if u=='[' or u=='(':s.append(u)
      elif u==']':
        if s[-1] == '[':s.pop()
        else:
          s=[1]
          break
      elif u==')':
        if s[-1] == '(':s.pop()
        else:
          s=[1]
          break
    print('no' if len(s) else 'yes')
  except:
    print('no')