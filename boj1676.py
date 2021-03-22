'''
백준 1676 - 팩토리얼 0의 개수
유형 : 수학
date = '2021-03-22'
'''

N = int(input())
factorial = 1
answer = 0
for i in range(1, N+1):
    factorial *= i
arr = list(str(factorial))
for j in range(len(arr) - 1, 0, -1):
    if int(arr[j]) == 0:
        answer += 1
    else:
        break
print(answer)