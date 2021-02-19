import math
L, A, B, C, D = int(input()), int(input()), int(input()), int(input()), int(input())
canC = math.ceil(A / C)
canD = math.ceil(B / D)
ans = max(canC, canD)
print(L-ans)
