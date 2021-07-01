'''
date 2021-07-01

15953 : 상금 헌터

문제 :
제이지는 자신이 코드 페스티벌에 출전하여 받을 수 있을 상금이 얼마인지 궁금해졌다. 그는 자신이 두 번의 코드 페스티벌 본선 대회에서 얻을 수 있을 총 상금이 얼마인지 알아보기 위해, 상상력을 발휘하여 아래와 같은 가정을 하였다.
제1회 코드 페스티벌 본선에 진출하여 a등(1 ≤ a ≤ 100)등을 하였다. 단, 진출하지 못했다면 a = 0으로 둔다.
제2회 코드 페스티벌 본선에 진출하여 b등(1 ≤ b ≤ 64)등을 할 것이다. 단, 진출하지 못했다면 b = 0으로 둔다.
제이지는 이러한 가정에 따라, 자신이 받을 수 있는 총 상금이 얼마인지를 알고 싶어한다.

Keyword :
자신의 등수에 따른 상금 금액을 합산해야한다.
'''
def prizeA(a):
    if a == 1:
        return 5000000
    elif 2 <= a <= 3:
        return 3000000
    elif 4 <= a <= 6:
        return 2000000
    elif 7 <= a <= 10:
        return 500000
    elif 11 <= a <= 15:
        return 300000
    elif 16 <= a <= 21:
        return 100000
    else:
        return 0


def prizeB(b):
    if b == 1:
        return 5120000
    elif 2 <= b <= 3:
        return 2560000
    elif 4 <= b <= 7:
        return 1280000
    elif 8 <= b <= 15:
        return 640000
    elif 16 <= b <= 31:
        return 320000
    else:
        return 0

testcase = int(input())
for i in range(testcase):
    a, b = map(int, input().split())
    print(prizeA(a)+prizeB(b))

