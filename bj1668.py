def cntTrophy(list1):
    flag = list1[0]  # 마지막 높이 값을 flag에 저장
    cnt = 1
    for i in range(1, len(list1)):
        if flag > list1[i]:  # 가려서 안 보이는 경우
            continue
        elif flag == list1[i]:
            continue
        else:  # 보이는 경우
            cnt += 1
            flag = list1[i]
    return cnt
'''
    # 같은 내용
    if flag < list1[i]:
        cnt += 1
        flag = list1[i]
'''

N = int(input())
trophyList = [int(input()) for _ in range(N)]
print(cntTrophy(trophyList))
# 반대면
trophyList.reverse()
print(cntTrophy(trophyList))
