while True:
    try:
        A, B, C = map(int, input().split())
        print(B - A - 1) if (B - A >= C - B) else print(C - B - 1)
    except EOFError:
        break