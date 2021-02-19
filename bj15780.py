N, K = map(int, input().split())
multi_tap = input().split()
total_multi = int(0) # 곶을 수 있는 멀티탭 구멍의 최대 개수
for i in multi_tap:
    total_multi += (int(i)+1) // 2

print('YES') if total_multi >= N else print('NO')