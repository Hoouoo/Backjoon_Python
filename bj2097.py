import math
N = int(input())
flag = math.floor(math.sqrt(N)) # 정사각형의 크기
#print('flag :', flag)
#print(N - (flag ** 2)) # 전체 개수에서 사각형 만큼의 개수를 뺌
if N < 4:
    print(4)
elif N - (flag ** 2) <= flag and N - (flag ** 2) != 0:# 직사각형에서 추가된 경우
    #print('#1')
    print((flag-1) * 2 + flag * 2)
elif math.sqrt(N) == flag :
    #print('#2')
    print((flag-1) * 4)
else:
    #print('#3')
    print(flag * 4)