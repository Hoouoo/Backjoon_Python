import sys
N = int(sys.stdin.readline())
arrN = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arrM = map(int, sys.stdin.readline().split())
for index in arrM:
    sys.stdout.write("1\n") if index in arrN else sys.stdout.write("0\n")