N = int(input())
N_list = list(map(int, input().split()))
flag = 0

if  len(N_list) == N:
    for i in N_list:
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt == 2:
            flag += 1
print(flag)
