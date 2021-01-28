N, P = map(int, input().split())
flag = N # 곱하는 수
ans = [0] * 98 # 주사위 S1, S2 와 비슷한 알고리즘을 활용하기 위해 0~ 98 가지의 의 배열 초기화 후 , 해당하는 인덱스 칸에 값이 존재할 때마다 + 1
while True:
    N = N * flag % P
    ans[N] += 1
    if ans[N] > 2:
        break
print(ans.count(2) + 1) # ans[N]이 올림이 되어 3이 된케이스를 포함시켜줘야 한다.
'''
    if list(map(lambda i: arr.count(i), arr)).count(3):
        print(list(map(lambda i: i, arr)))
        #print(set(arr))
        break
        # print(list(map(lambda i: arr.count(i), arr))) # 테스트 코드
'''
'''
while True:
    if list(map(lambda i: arr.count(i), arr)).count(2):
        if ans == 2: # 중복되는 수가 없다.
            print(0)
            break
        else:
            print(ans - 1)
            break
    else:
        N = N * flag % P
        arr.append(N)
        ans += 1
        # print(list(map(lambda i: arr.count(i), arr))) # 테스트 코드
'''
