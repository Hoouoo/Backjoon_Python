import sys
input = sys.stdin.readline
n = int(input())
stack: list = []
operator: list = []
cnt = 1
flag = True
for i in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        operator.append('+')
        cnt += 1
    if stack[-1]==num:
        stack.pop()
        operator.append('-')
    else:
        flag = False
if flag == False:
    print('NO')
else:
    for idx in operator:
        print(idx)
