'''
문제이해 :
첫 번째 입력은 테스트 케이스의 개수 T
두 번째 입력은 테스트 케이스에 대해 정수 a와 b이며, a^b로, 밑수 일의 자리 규칙을 이용한다.
밑수 처리 공식은 다음과 같다
1 : 1
2 : 2486
3 : 3971
4 : 46
5 : 5
6 : 6
7 : 7931
8 : 8426
9 : 91
'''
testCase = int(input())
a:list = [] # a = []
b:list = [] # b = []

# 테스트 케이스 만큼 a와 b에 삽입
for _ in range(testCase):
    tmpA, tmpB = map(int, input().split())
    a.append(tmpA)
    b.append(tmpB)

# 삽입된 배열 a와 b의 승수의 패턴에 따라 결과 값 출력
for idx in range(testCase):
    base = a[idx] % 10
    if base == 0:
        print(10)
    elif base in [1, 5, 6]:
        print(base)
    elif base in [4, 9]:
        if b[idx] % 2 == 0: ## 0 승은 1이다.
            print(base ** 2 % 10)
        else:
            print(base)
    else:
        if b[idx] % 4 == 0:
            print(base ** 4 % 10)
        else:
            print(base ** (b[idx] % 4) % 10)



