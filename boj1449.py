N, L = map(int, input().split())
pl = list(map(int, input().split()))

pl.sort()
ans = 0; tmp =0
for idx in pl:
    if tmp < idx:
        ans += 1
        tmp = idx + L - 1
print(ans)