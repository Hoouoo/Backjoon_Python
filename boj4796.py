index = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    #ans = V - (V // P * (P - L))
    ans = V // P * L + L if V % P >= L else V - (V // P * (P - L))
    print('Case ' + str(index) +  ': ' + str(ans))
    index += 1