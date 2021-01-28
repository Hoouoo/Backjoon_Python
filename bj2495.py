final_ans = []
for _ in range(3):
    arr = input()
    arr = list(map(int, arr))
    flag = arr[0] # 같은지 판단하기 위한 기준
    ans = []
    for i in range(1, len(arr)):
        if flag == arr[i]:
            ans.append(arr[i])
        elif flag != arr[i]:
            flag = arr[i]
    # print(ans)
    cnt = [0] * 10
    for i in range(1,  10): # 1~10의 숫자까지 돌림
        cnt[i] = ans.count(i) # 1~10 까지의 수 배열 인덱스에 해당하는 중복되는 숫자 입력
        # print(cnt)
    final_ans.append((max(cnt)+1)) if max(cnt) > 0 else final_ans.append(1)

for answer in final_ans:
    print(answer)

