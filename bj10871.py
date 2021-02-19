N, X = map(int,input().split())
A = list(map(int, input().split()))
for i in A:
    print(i, end=' ') if i < X else None