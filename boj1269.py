import sys
input = sys.stdin.readline
A, B = map(int, input().split())
arrA = set(map(int, input().split()))
arrB = set(map(int, input().split()))
ans = []
for idx in arrA:
    if idx not in arrB:
        ans.append(idx)
for idx in arrB:
    if idx not in arrA:
        ans.append(idx)
print(len(ans))