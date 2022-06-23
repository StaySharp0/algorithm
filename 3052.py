print(len(set(a % 42 for a in map(int,[*open(0)]))))

# print(len({int(i)%42for i in open(0)}))
# set 대신 {} 활용
# 굳이 map(int,[*open(0)]) 안해도 됬음