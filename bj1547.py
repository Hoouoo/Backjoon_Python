M = int(input())
cup = [1, 2, 3]

for _ in range(M):
    x, y = map(int, input().split())
    x1 = cup.index(x) #cup x 인덱스 값 반환
    y1 = cup.index(y) #cup y 인덱스 값 반환
    cup[x1], cup[y1] = cup[y1], cup[x1] # cup[x1], cup[y1] 인덱스 위치 서로 교환
print(cup[0])