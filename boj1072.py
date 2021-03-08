from math import floor
import sys
input = sys.stdin.readline
x, y = map(int, input().split())
e = floor(100 * y / x)
low, high = 0, 1000000000
if e >= 99:
    print(-1)
else:
    while low <= high:
        mid = (low + high) // 2
        x1, y1 = x + mid, y + mid
        if floor(100 * y1/x1) > e:
            # print('high', high, 'e : ', e, 'x1 : ', x1, 'y1 : ', y1)
            high = mid -1
        else:
            # print('low', low)
            low = mid + 1
    print(high + 1)