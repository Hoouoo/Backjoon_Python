'''
boj 1183
# Date : 2021 - 02 - 07
# Silver 5
'''

'''
문제 이해:

쉽게말하면 배열의 중앙점을 찾아야 한다.
홀수는 1개로 떨어지며, 짝수는 범위 내의 모든 수가 해당한다. 
'''
N = int(input())
X = [] # S[i] - A[i]
for _ in range(N):
    Stmp, Atmp = map(int, input().split())
    X.append(Stmp-Atmp)
    #print(X)
X.sort()
#print(X)
if N % 2 != 0:
    print(1)
else:
    print(abs(X[N // 2] - X[N // 2 -1]) +1)