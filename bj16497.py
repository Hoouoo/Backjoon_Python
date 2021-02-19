N = int(input())
out = [list(map(int, input().split())) for i in range(N)]
K = int(input())
cnt = 0
day = [True] * 32
for i in range(len(out)):
    if out[i][0] <= out[i][1]:
        if day[(out[i][0])] and K >= 1:
            K -= 1
            #print(K)
            for j in range(out[i][0], (out[i][1]+1)):
                day[j] = False
                if out[i][1] == j:
                    day[j] = True
                    K += 1
                   # print('#2 K:',day[j], ' !!', K)
        else:
            K -= 1
print(1) if K  > 0 else print(0)
