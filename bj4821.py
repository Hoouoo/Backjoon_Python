while True:
        N = int(input())
        if N == 0:
            exit()
        P = list(input().split(','))
        ans = [0] * (N+1) # 중복검사용

        for i in range(len(P)):
            if '-' in P[i]:
                low, high = map(int, P[i].split('-'))
                if low <= high:
                    if low <= N:
                        if high <= N: # N 보다 high 가 작은경우
                            for j in range(low, high+1):
                                #print('case 1 : ', j)
                                ans[j] = 1
                        else:# 큰경우
                            high = N # N에 맞춰준다.
                            for j in range(low, high+1):
                                #print('case 2 : ', j)
                                ans[j] = 1
            else:
                if int(P[i]) <= N:
                    #print('case 3 : ', i)
                    ans[int(P[i])] = 1
        print(sum(ans))

'''
while True:
    try:
        N = int(input())
        if N == 0:
            exit()
        P = list(input().split(','))
        renewP = []
        maxP = [False] * 1000  # 출력된 페이지 확인
        ans = 0
        for i in P:
            renewP.append(list(map(int, i.split('-'))))
        for i in renewP:
            if len(i) > 1:
                if i[1] >= i[0] and maxP[i[1]] == False:
                    for j in range(i[0], i[1] + 1, 1):  # 10~ 16 으로해야지 10 - 15로 탐색
                        if not maxP[j] and j <= N:  # 페이지 보다 작아야함
                            # print('low : ', i[0], 'high : ', i[1], '//// ' , j, 'ans : ', ans)
                            maxP[j] = True
                            # print(j, maxP[j])
                            ans += 1
            else:
                if i[0] <= N and maxP[i[0]] == False:
                    # print('low : ', i[0] , 'ans : ', ans)
                    ans += 1
                    maxP[i[0]] = True
        print(ans)
    except IndexError:
        pass

'''