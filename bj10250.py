'''
T = int(input())
square = [input().split() for _ in range(T)]
for h, w, n in square:
    host = int(1) + (int(n) // int(h)) + (int(100) * (int(n) % int(h))) if int(n) % int(h) != 0 else int(100) + (int(n) // int(h)) + (int(100) * (int(n) % int(h))) if int(n) % int(h) == int(0) else None
    print(host)
'''
t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    num = n//h + 1
    floor = n % h
    if n % h == 0:  # h의 배수이면,
        num = n//h
        floor = h
    print(floor*100+num)

