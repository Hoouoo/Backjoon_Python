N = int(input())
arr = list(map(int, input().split()))
flag = arr[0]
upper = [] # 오르막으롳 추정되는 값 저장
upperFlag = 0 # upper의 마지막 값 기록
ans = []  # 측정된 오르막길 값

for i in range(len(arr)):
    if flag < arr[i]:
        #print('test flag: ', flag)
        upper.append(arr[i-1]) if len(arr) > 0 else None
        upper.append(arr[i])
        #print('test upper:', upper)
        if i == (len(arr) - 1) : # 인덱스 마지막 탐색인 경우
            ans.append(upper[-1] - upper[0]) if len(upper) > 0 else None  # 해주지 않으면 인덱스 오류 발생 인덱스 범위 오류
            upper.clear()
        flag = arr[i]
    else:
        #print('flag : ', flag ,'upperFlag : ', upperFlag)
        ans.append(upper[-1] - upper[0]) if len(upper) > 0 and flag != arr[i] and upper[0] != upperFlag else None # 다음 숫자가 i랑 같아서도 안되고, 앞에 숫자가 전에 값과 같아선 안됨
        upperFlag = upper[-1] if len(upper) > 0 else 0
        #print('ans : ', ans)
        upper.clear()
        flag = arr[i]
#print(ans)
print(0) if not ans else print(max(ans)) # 빈경우 0 아닌경우 ans 출력
