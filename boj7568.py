N = int(input())
arrHeightWeight = [list(map(int, input().split())) for _ in range(N)]
for first in arrHeightWeight: # loop arrHeightWeight
    rank = 1
    for second in arrHeightWeight: # loop (loop arrHeightWeight index)
        if first[0] < second[0] and first[1] < second[1]:
            rank += 1
        # print(first[0], first[1], second[0], second[1])

    print(rank, end=' ')
