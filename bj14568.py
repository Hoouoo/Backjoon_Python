# 해당 문제는 까다로운 택희의 기준에 맞추면 된다.
N = int(input())
ans = 0
for i in range(2, N-1, 2):
    ans += (N-i-2) // 2 # 욕심쟁이 택희의 경우의 수
print(ans)

