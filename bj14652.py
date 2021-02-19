import math
seat = list(map(int, input().split()))
height = math.floor(seat[2]/seat[1])
width = seat[2] % seat[1]

print(height, width, end=' ')
