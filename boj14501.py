N = int(input())
day = []
cost = []
maximumCost = []
for idx in range(N):
    a, b = map(int, input().split())
    day.append(a)
    cost.append(b)
    maximumCost.append(b)
maximumCost.append(0)
# print(maximumCost)
for idx in range(N-1,-1,-1): # index range 0 - 9
    if day[idx] + idx > N: # bc, 0 - 9 범위기 때문에 N 보다 커야한다. / 일 수가 최대 일수를 벗어나는 경우
        maximumCost[idx] = maximumCost[idx + 1]
        # print(idx, maximumCost[idx])
    else:
        # 최대 비용은 현재 날짜 + 현재 날짜에 종료 시점의 비용 vs 이전까지의 최대 비용
        maximumCost[idx] = max(maximumCost[idx+1], cost[idx] + maximumCost[idx + day[idx]])
        # print(idx, maximumCost[idx], idx+day[idx], maximumCost)
print(maximumCost[0])