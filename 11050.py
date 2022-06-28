# https://www.acmicpc.net/problem/11050
# 5 2
# 10
# https://shoark7.github.io/programming/algorithm/3-ways-to-get-binomial-coefficients
# 해당 방법 학습해서 개선 
n, k = map(int, input().split())

def dp(n, k):
    if k > n: return 0

    C = [[-1]*(n+1) for _ in range(n+1)] # [[-1]*(n+1)]*(n+1) 배열 참조가 복사되서 제대로 안나옴

    def choose(times, got):
      if times == n:
	      return got == k

      if C[times][got] != -1:
	      return C[times][got]

      C[times][got] = choose(times+1, got) + choose(times+1, got+1)
      return C[times][got]
      
    return choose(0, 0)

print(dp(n,k))