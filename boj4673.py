'''
유형 : 수학, 구현
4673 : 셀프 넘버
Date 2021-07-17
Keywords : 셀프 넘버 구하기
'''
a = set(range(1, 10001))
b = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    b.add(i)
answer = sorted(a - b)
for k in answer:
    print(k)