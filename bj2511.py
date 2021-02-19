A = list(map(int, input().split()))
B = list(map(int, input().split()))
scoreA = scoreB = 0
flag = 0
for i in range(0, 10):
    if A[i] > B[i]:
        scoreA += 3
        flag = i
    elif A[i] < B[i]:
        scoreB += 3
        flag = i
    else:
        scoreA += 1
        scoreB += 1
print(scoreA, scoreB)
if scoreA == scoreB:
    if A[flag] > B[flag]:
        print('A')
    elif A[flag] < B[flag]:
        print('B')
    else:
        print('D')
elif scoreA > scoreB:
    print('A')
else:
    print('B')


''' 
#간단한 소스
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
state=''    # 이긴 사람의 이름 혹은 D가 순서대로 추가될 string
for i in range(10):   # 경기를 차례대로 돌며 이긴 사람을 state에 기록
    a,b = A[i],B[i]
    if a>b:
        state += 'A'
    elif a<b:
        state += 'B'
    else:
        state += 'D'

# total 점수 계산은 string인 state에 count를 적용해 계산
equal = state.count('D')  
total_A = state.count('A')*3 + equal
total_B = state.count('B')*3 + equal
print(total_A, total_B)

# total_A와 total_B의 비교에서 같은 경우를 먼저 처리해줘야 런타임 에러가 안남
if total_A == total_B:
    final_state = state.replace('D','')
    if len(final_state) != 0:
        print(state.replace('D','')[-1])  # 'D' 지우고 가장 마지막 승자 추출
    else:
        print('D')
elif total_A > total_B : print('A')
else : print('B')
'''