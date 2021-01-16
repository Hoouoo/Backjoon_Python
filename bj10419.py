import math
T = int(input())
s = [int(input()) for _ in range(T)]
for i in s:
    print(math.floor(math.sqrt(i))) if (math.floor(math.sqrt(i)) ** 2 + math.floor(math.sqrt(i))) <= i else print(math.floor(math.sqrt(i)) - 1)