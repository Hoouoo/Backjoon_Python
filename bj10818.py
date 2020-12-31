N = int(input())
N_list = list(map(int, input().split())) # == N_list = []
N_list.sort()
print(N_list[0], N_list[len(N_list)-1])

# 속도 빠른 방법
"""N = int(input()) 
N_list = list(map(int, input().split())) # == N_list = []
print('{} {}'.format(min(N_list),max(N_list)))"""