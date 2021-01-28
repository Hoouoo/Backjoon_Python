N = int(input())
fileSize = list(map(int, input().split()))
diskSize = int(input())
cnt = 0
for i in fileSize:
    if i % diskSize == 0: # 딱 떨어지는 경우
        cnt += i // diskSize
    else: # 아닌 경우 클러스터 공간이 나눈 몫보다 한개 더필요하다.
        cnt += i // diskSize + 1
print(diskSize * cnt)