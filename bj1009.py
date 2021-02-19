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
[Tip]
** : 거듭제곱 연산자
'''
a = []
b = []
T = int(input())
for _ in range(T):      #T 만큼 입력 a와 b 입력
    numA, numB = map(int, input().split())
    a.append(numA)
    b.append(numB)
for i in range(T):
    base = a[i]%10 # 밑수의 범위는 1~10이므로
    if base == 0:
        print(10)
    elif base  in [1, 5, 6]: # 1,5,6이 안에 있으면
        print(base)
    elif base in [4, 9]:
        if b[i] % 2 == 0:
            print(base ** 2 % 10)
        else:
            print(base)
        # 첫 번째 수가 4는 4로 시작하고 9는 9로시작하므로 base를 써도 무관하다. == base**(b[i]%2)%10
    else:
        if b[i]%4 == 0: # 4번씩 순환하니까
            print(base ** 4 % 10) # %4 ==0 이면 **4를 해준것과 같다.
        else:
            print(base**(b[i] % 4) % 10)
