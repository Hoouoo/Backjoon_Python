N, K = map(int, input().split())
for index in range(1, K+1):
    N -= index
    # print('N : ', N, 'index : ', index)
if N < 0: # ex) input : 5 3 기준  1 2 3보다 -1 부족함
    print(-1)
elif N % K == 0: # N % K인 경우에만 K-1 값이 나옴
    print(K-1)
else:
    print(K)
