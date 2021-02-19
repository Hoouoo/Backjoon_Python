import math

starfruits = list(map(int, input().split()))
harvest = math.floor((starfruits[0]-1)/starfruits[1]) * starfruits[2]
ans = starfruits[3] * harvest
print(ans)