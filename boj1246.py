'''
Date : 2021-02-09
boj 1246 / Silver 5
'''
N, M = map(int,input().split())
arr = [int(input()) for _ in range(M)] # customer price arr
arr.sort()
revenue = []
ans = 0
ansPrice = 0
for price in range(M):
    flag = arr[price]
    cnt = len(list(filter(lambda x: flag <= x, arr)))
    if cnt > N: # cnt must lower than N
        cnt = N
    revenue.append(arr[price] * cnt)
    ans = max(revenue)
    if (arr[price] * cnt) == ans:
        ansPrice = arr[price]
print(ansPrice, ans)