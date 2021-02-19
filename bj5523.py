import sys
N = int(input())
cnt_A = cnt_B = int(0)
for i in range(N):
    Ai, Bi = map(int, sys.stdin.readline().split())
    if Ai > Bi:
        cnt_A += 1
    elif Ai < Bi:
        cnt_B += 1
print(cnt_A, cnt_B)