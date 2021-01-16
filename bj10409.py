n, T = map(int, input().split())
time = list(map(int, input().split()))
cnt = int(0)
for i in time:
    T -= i
    if T >= 0:
        cnt += 1
print(cnt)