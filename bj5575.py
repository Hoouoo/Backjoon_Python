for i in range(3):
    aH, aM, aS, bH, bM, bS = map(int, input().split())
    aTime = (aH * 3600) + (aM * 60) + aS
    bTime = (bH * 3600) + (bM * 60) + bS
    check = bTime - aTime
    print((check // 3600), (check % 3600  // 60), (check % 3600 % 60))