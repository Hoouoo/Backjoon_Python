X, Y, W , S = map(int, input().split())

# 평행선으로만 가는 경우
result1 = (X+Y) * W

# 대각선으로 가는 경우 짝 / 홀 (대각선으로 최대 이동 후 한칸 이동 \/\/\ 이렇게 이동가능
result2 = max(X,Y) * S if (X+Y) % 2 == 0 else ((max(X, Y) - 1) * S) + W

# 대각선으로 최대한 가고 평행선으로 가는경우
result3 = ((min(X, Y)) * S) + (abs(X-Y) * W)
#print(result1)
#print(result2)
#print(result3)
print(min(result1, result2, result3))
'''
X, Y, W , S = map(int, input().split())

# 평행선으로만 가는 경우
result1 = (X+Y) * W

# 대각선으로 가는 경우 / # 대각선으로 최대한 가고 평행선으로 가는경우
result2 = X * S if X == Y else ((min(X, Y)) * S) + (abs(X-Y) * W)

print(result1)
print(result2)
print(result1) if result1 < result2 else print(result2)

'''