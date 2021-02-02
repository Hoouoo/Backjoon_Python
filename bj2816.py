N = int(input())
channel = [input() for _ in range(N)]
#remoteCtrl = list(map(int, [1, 2, 3, 4]))
#print(remoteCtrl)

# 1. 화살표를 한 칸 아래로 내린다. (i > i+1)
# 2. 화살표를 위로 한 칸 올린다(i>i-1)
# 3. 현재 선택한 채널을 한 칸 아래로 내린다. (i <> i+1 , 커서는 i+1)
# 4. 현재 선택한 채널을 위로 한 칸 올린다. (1 <> i-1, 커서는 i+1)
print(channel)
flag = 0
while channel[0] != 'KBS1' and channel[1] != 'KBS2':
    if channel[flag] != 'KBS1':
