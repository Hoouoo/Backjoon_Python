'''
14912 : 숫자 빈도수
Date 2021-07-04

구현 : 구현, 브루트 포스 알고리즘
keyword:
입력받은 숫자의 빈도수를 찾아야한다.
'''

a, find = map(int, input().split())
answer = 0
for i in range(1, a+1):
    for j in str(i):
        if str(find) in j:
            answer += 1
print(answer)

