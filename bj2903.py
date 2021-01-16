import math

N = int(input())
start = 2
final = 0
for i in range(0, int(N)):
    final = (start + (start-1)) ** 2
    start = int(math.sqrt(final))
print(final)