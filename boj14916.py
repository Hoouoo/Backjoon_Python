'''
date : 2021-02-19
algorithm : math, dynamic programing, greedy, brute force

boj 141916
'''

N = int(input())
mod = N % 5
ans = 0
if N == 1 or N == 3:
    ans = -1
    print(ans)
elif mod % 2 == 0:
    ans = (N // 5) + (N % 5 // 2)
    print(ans)
else:
    ans = (N // 5 - 1) + ((N - (N // 5 -1 ) * 5 ) // 2)
    print(ans)



