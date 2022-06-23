# 꼭대기까지 위로 이동, 오른쪽 한칸 이동
for h,w,x in [map(int, l.split()) for l in [*open(0)][1:]]:
  print('%d%02d' % (h if (a:=x%h) == 0 else a, x//h + (a != 0)))

# 2
# 6 12 10
# 30 50 72
# 6 12 6
# 6 12 12
# 6 12 72
# 끝에 고려 안했음 ㅠ
# for r in[*open(0)][1:]:h,_,n=map(int,r.split());n-=1;print((n%h+1)*100+n//h+1)