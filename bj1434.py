N,M = map(int, input().split())
Aj = list(map(int, input().split()))
Bj = list(map(int, input().split()))
total_Aj = 0
total_Bj = 0
for i in Aj:
    total_Aj += i
for i in Bj:
    total_Bj += i
print(total_Aj - total_Bj) if total_Aj >= total_Bj else None