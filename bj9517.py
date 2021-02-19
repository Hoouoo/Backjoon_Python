'''
K = int(input())-1
N = int(input())
cnt = int(210)
flag = int(0)
for _ in range(N):
    time, ans = input().split()
    time = int(time)
    if ans == 'T':
        cnt -= time
        if flag == 0 and cnt <= 0:
            flag = (K+1) % 8
        K += 1
    else:
        cnt -= time
        if flag == 0 and cnt <= 0:
            flag = K % 8
print(flag)
'''
i = int(input())-1
q = [input().split() for _ in range(int(input()))]
tt = 0
for t, ans in q:
    tt += int(t)
    if tt >= 210:
        print(i+1)
        break
    if ans == 'T':
        i = (i + 1)%8
print(q)