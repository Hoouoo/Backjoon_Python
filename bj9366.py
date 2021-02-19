T = input()
for i in range(int(T)):
    A, B, C = map(int, input().split())
    maxNum = max(A, B, C)
    remainNum = A + B + C - maxNum
    if remainNum > maxNum:
        if A == B == C:
            print('Case #{}: equilateral'.format(i+1))
        elif A == B != C or A == C != B or B == C != A:
            print('Case #{}: isosceles'.format(i+1))
        else:
            print('Case #{}: scalene'.format(i+1))
    else:
        print('Case #{}: invalid!'.format(i + 1))

# 참고할만한 소스
'''
def cc(l): return 1 if l[2] < l[1]+l[0] else 0 # 가장 큰변 < 나머지 두변
for i in range(int(input())):
	a,b,c = map(int, input().split())
	print('Case #{}: {}'.format(i+1, 'invalid!' if not cc(sorted([a,b,c])) else 'equilateral' if a==b==c else 'isosceles' if a==b or b==c or a==c else 'scalene'))
'''