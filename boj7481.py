N = int(input())
for _ in range(N):
    a, b, S = map(int, input().split())
    check = [False] * (S + 1)
    if a + b < S:
        for idx in range(0, a + b + 1): # 1개씩은 무조건 포함해야함)
            check[idx] = True
            print(check)
        if max(a, b) == b: # a가 작을 때
            maxCnt = 1
            minCnt = 1
            flag = 0
            for cnt in range(check.index(False), S+1, b):
                maxCnt += 1
                print(cnt)
                flag = cnt
            for cnt in range(check.index(False), flag+1):
                check[cnt] = True
                print(maxCnt, '#Max', check)

            for cnt in range(check.index(False), S+1, a):
                check[cnt] = True
                minCnt += 1
                print(minCnt // a, '#Min', check)

    print(check)

