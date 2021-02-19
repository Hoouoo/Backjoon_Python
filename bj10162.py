time = int(input())
A, B, C = int(300), int(60), int(10)
if (time % A % B % C) != 0:
    print(-1)
else:
    print((time // A), (time % A // B), (time % A % B // C))