S1, S2, S3 = map(int, input().split(' ')) #S1, S2, S3 입력

arr = [0] * (S1 + S2 + S3 + 1) # 주사위의 각각 합에 해당하는 배열

for i in range(1, S1 + 1): # 첫째자리
    for j in range(1, S2 + 1): # 둘째자리
        for k in range(1, S3 + 1): # 셋째자리
            arr[i + j + k] += 1 # 해당하는 부분 카운트 + 1

flag = 0
ans = 0
for i in range(S1 + S2 + S3 + 1):
    if flag == arr[i]:
        continue
    elif flag < arr[i]:
        flag = arr[i]
        ans = i
print(ans)