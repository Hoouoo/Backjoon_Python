import sys

line = 20


# 스위치 한줄에 20개 씩
def girl_algorithm(arr, idx_tmp):
    left, right = idx_tmp - 1, idx_tmp + 1
    min_left, max_right = idx_tmp, idx_tmp
    while left > 0 and right < len(arr):
        if arr[left] == arr[right]:
            min_left, max_right = left, right
            left -= 1
            right += 1
        else:
            break
    return max(idx_tmp - min_left, max_right - idx_tmp)


N_first = int(sys.stdin.readline())
arrSwitch = list(map(int, sys.stdin.readline().split()))
# 길이와 idx 값을 맞춰주기 위함
arrSwitch.insert(0, -1)
# print(arrSwitch)
N_second = int(sys.stdin.readline())
for _ in range(N_second):
    sex, idx = map(int, sys.stdin.readline().split())
    # Men
    if sex == 1:
        for idx in range(idx, len(arrSwitch), idx):
            # print(idx, len(arrSwitch))
            arrSwitch[idx] = (arrSwitch[idx] + 1) % 2
        # print(idx)

    elif sex == 2:
        len_max = girl_algorithm(arrSwitch, idx)
        tmp = arrSwitch[idx - len_max: idx + len_max + 1]
        # print('len_max = ', len_max,'idx = ', idx , 'tmp', tmp, 'arr = ', arrSwitch)

        for i in range(len(tmp)):
            tmp[i] = (tmp[i] + 1) % 2

        arrSwitch[idx - len_max: idx + len_max + 1] = tmp

for idx in range(1, len(arrSwitch), line):
    print(*arrSwitch[idx: idx + line])
    # * 하나는 키 값 출력
    # ** 두개는 value 값 출력하는데 value 사용시 반드시 키 값을 명시해야한다.
