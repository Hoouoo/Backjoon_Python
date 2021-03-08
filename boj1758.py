N = int(input())
ans = 0
tip = [int(input()) for _ in range(N)]
tip.sort(reverse=True)
for order in range(1, len(tip)+1):
    tmp = tip[order-1] - (order - 1)
    if tmp > 0:
        ans += tmp
print(ans)