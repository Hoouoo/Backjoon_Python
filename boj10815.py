import sys
N = int(sys.stdin.readline())
arrN = set(map(int, sys.stdin.readline().split()))
print(arrN)
M = int(sys.stdin.readline())
arrM = list(map(int, sys.stdin.readline().split()))
for index in arrM:
    sys.stdout.write("1 ") if index in arrN else sys.stdout.write("0 ")

# # 이진 탐색
# n = int(input())
# a = list(map(int, input().split()))
# a.sort()
#
# def binary_search(num):
#     l = 0
#     r = n-1
#     while l <= r :
#         mid = (l+r)//2
#         if a[mid] == num :
#             return 1
#         elif a[mid] > num :
#             r = mid - 1
#             # 반 줄여주기 1
#         else:
#             l = mid + 1
#             # 반 줄여주기 2
#     return 0
#
# input()
# for num in list(map(int, input().split())):
#     print(binary_search(num), end = ' ')