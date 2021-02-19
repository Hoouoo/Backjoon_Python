K, L = map(int, input().split())
val = list(map(int, range(0, L+1)))
ans = 0
for i in range(2, int((L ** 0.5)+1)):
    if val[i]:
        val[1] = 0 # 1은 삭제
        for j in range(i*2, L+1, i):
            val[j] = 0
for i in val:
    if i > int(1) and K % i == int(0):
        if i != L:
            ans = i
            print('BAD', ans)
            exit()
if ans == 0:
    print("GOOD")
