S = list(map(int, input().split()))
cost_S = S[0] * 10 - 500 if S[0] * 10 >= 5000 else S[0] * 10 # 10 봉지의 값이 5000원 이상이면 500원 할인 아니면 그냥 곱하기 10
cost_S = S[1] / cost_S  # 가성비를 구하는 공식
N = list(map(int, input().split()))
cost_N = N[0] * 10 - 500 if N[0] * 10 >= 5000 else N[0] * 10
cost_N = N[1] / cost_N
U = list(map(int, input().split()))
cost_U = U[0] * 10 - 500 if U[0] * 10 >= 5000 else U[0] * 10
cost_U = U[1] / cost_U

print('S') if max(cost_S, cost_N, cost_U) == cost_S else print('N') if max(cost_S, cost_N, cost_U) == cost_N else print('U')