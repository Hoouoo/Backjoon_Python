'''
11047 : 동전 0
Date 2021-07-10

유형 : 그리디
'''
N, K = map(int, input().split())
count = 0
coin_types = list(int(input()) for i in range(N))
coin_types = coin_types[-1::-1]
for coin in coin_types:
    # if K >= coin:
    count += K // coin
    K %= coin
print(count)
