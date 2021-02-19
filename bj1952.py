M, N = map(int, input().split())# 열 : col (M) / 행 : row (N)
snail = [[0 for row in range(N)] for col in range(M)]
moveC = [0, 1, 0, -1]
moveR = [1, 0, -1, 0]
# 1,0 : 우 / -1, 0 : 하 / 0,1 : 좌  / 0,-1 : 상
r = c = ans = dir = int(0)
MAP = M*N
while True:
    if snail[c][r]:
        print(ans-1)
        break
    snail[c][r] = 1
    nextC = c + moveC[dir]
    nextR = r + moveR[dir]

    if(nextC < 0 or nextR < 0 or nextC >=M or nextR >=N or snail[nextC][nextR]):
        dir = (dir+1) % 4
        nextC = c + moveC[dir]
        nextR = r + moveR[dir]
        ans += 1
    c = nextC
    r = nextR

