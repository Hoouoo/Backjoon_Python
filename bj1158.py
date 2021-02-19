'''
boj 1158
1 2 3 4 5 6 7 / 요세 푸스 순열 : 3
    x     x
  x         x
        x
x     x
'''
'''
peopleCnt, loop = map(int, input().split())
Yosepuse = [False] * (peopleCnt + 1)
Yosepuse[0] = True
idx = 0
cnt = 0
print("<", end = '')
while True:
    cnt += 1
    if cnt == loop:
        idx = idx + loop if (idx + loop) <= peopleCnt else loop - (peopleCnt - idx)
        if not Yosepuse[idx]:
            print(idx, end = ', ')
            Yosepuse[idx] = True
            cnt = 0
            #print(idx, Yosepuse[idx])
        else:
            cnt -= 1
    if len(list(filter(lambda x : x == True, Yosepuse))) == peopleCnt:
        break
print('\b\b', end='') # erase
print(">")
'''
N,K=map(int,input().split())
l=[* range(1,N+1)]
print(l)

