'''
백준 1065번 : 한 수
알고리즘 : 브루트포스 알고리즘

date : 2021-03-16
'''
# 등차 수열인 수를 '한 수'라고 한다
# ex) 1 2 / 1 2 3 / 2 4 6
N = int(input())
ans = 0
for i in range(1, N+1):
    # 1의자리 ~ 100의자리까지 자리수 구분
    c = i // 100
    b = i % 100 // 10
    a = i % 100 % 10
    #print(c, b, a)
    # 10의 자리 수까지는 등차수열 상관 X
    if c == 0:
        #print('#1', i)
        ans += 1
    # 100부터는 각 자리의 수가 등차 수열로 구성 되야 함
    elif c - b == b - a:
        #print('#2', i)
        ans += 1
print(ans)
