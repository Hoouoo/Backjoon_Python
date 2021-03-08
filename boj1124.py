'''
date : 2021-03-08

algorithm : 수학, 정수론, 소수 판정
'''
import sys
import math

arr = []
n = 100001
arr = [True for i in range (n+1)]

for i in range(2, int(math.sqrt(n))):
    if arr[i] == True: # i 가 소수인 경우
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            arr[i * j] = False
            j += 1
for i in range(2, n):
    if arr[i]:
        arr.append(i)

input = sys.stdin.readline
A, B = map(int, input().split())
ans = set()
for num in range(A, B+1):
    i = 2 # 소인수 분해를 위한 변수
    i2 = 2 # flag 소인수 분해
    # print('[ ] ',num,end=' ')
    cpNum = num
    flag = 0
    while cpNum != 1:
        if cpNum % i == 0:
            cpNum = cpNum / i
            flag += 1
            # print(num, flag)
        else:
            i += 1
    if flag != 1 and flag in arr:
        ans.add(num)
# print(ans)
sys.stdout.write('{}'.format(len(ans)))


# import math
#
# def is_prime_number(x):
#     for i in range(2, int(math.sqrt(x)) + 1):
#         if x % i == 0:
#             return False
#     return True
#
#
#
# print(is_prime_number(2))
# print(is_prime_number(3))