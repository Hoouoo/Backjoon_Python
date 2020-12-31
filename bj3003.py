Chess = (1, 1, 2, 2, 2, 8)
my_chess = list(map(int, input().split()))
ans = 0
for i in range(0, len(Chess)):
    ans = Chess[i] - my_chess[i]
    print(ans, end=' ')
