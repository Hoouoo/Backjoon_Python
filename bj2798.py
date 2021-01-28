N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

for i in arr[0:N-2]:
    for j in arr[arr.index(i) + 1:N-1]:
        for k in arr[arr.index(j) + 1:N]:
            if i + j + k > M:
                continue
            else:
                ans = max(ans, i + j + k)
print(ans)
