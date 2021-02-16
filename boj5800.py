'''
date : 2021-02-16
boj5800

# 정렬
'''
from itertools import combinations

K = int(input())
for index in range(K):
    Largest_gap = int(0)
    arr = list(map(int, input().split()))
    del arr[0]
    arr.sort()
    # print(arr)
    for cnt in range(1, len(arr)):
        Largest_gap = max(abs(arr[cnt-1]-arr[cnt]), Largest_gap)
        # print(Largest_gap)
    # arr.reverse() # 앞 숫자 삭제 후 정렬
    Max, Min = arr[-1], arr[0],
    print('Class', index+1)
    print('Max {}, Min {}, Largest gap {}'.format(Max, Min, Largest_gap))

