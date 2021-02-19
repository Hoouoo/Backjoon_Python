N = int(input())
channel = [input() for _ in range(N)]
#remoteCtrl = list(map(int, [1, 2, 3, 4]))
#print(remoteCtrl)
idxKBS1 = 0 # KBS1 idx
idxKBS2 = 0 # KBS2 idx
# 1. 화살표를 한 칸 아래로 내린다. (i > i+1)
# 2. 화살표를 위로 한 칸 올린다(i>i-1)
# 3. 현재 선택한 채널을 한 칸 아래로 내린다. (i <> i+1 , 커서는 i+1)
# 4. 현재 선택한 채널을 위로 한 칸 올린다. (1 <> i-1, 커서는 i+1)
for idx in channel:
    if idx == 'KBS1':
        idxKBS1 = channel.index(idx)
    elif idx == 'KBS2':
        idxKBS2 = channel.index(idx)
ans = ''
ans += '1' * idxKBS1
ans += '4' * idxKBS1
if idxKBS1 > idxKBS2: # KBS1 is lower than KBS2
    idxKBS2 += 1 # KBS2 idx + 1
ans += '1' * idxKBS2
ans += '4' * (idxKBS2-1) # KBS2 idx located second
print(ans)

