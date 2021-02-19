N, find = map(int, input().split())
medalList = [list(map(int, input().split())) for _ in range(N)]
medalList.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)
flag = 0
for index in range(N):
    if medalList[index][0] == find:
        flag = index
for index in range(N):
    if medalList[index][1:] == medalList[flag][1:]:# if 금, 은, 동메달이 같은경우 중복된
        print(index + 1)
        break
