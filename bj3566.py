import math
demandMonitor = list(map(int, input().split()))
N = int(input())
myMonitor = [list(map(int, input().split())) for _ in range(N)]
flagH = flagV = 0 # 가로세로 flag 값
rflagH = rflagV = 0 # 가로세로 반대
diffPrice = [] # 모니터 가격비교
for i in range(N):
    for j in range(0, 4, 2):
        #print(j)
        flagH = max(math.ceil(demandMonitor[j] / myMonitor[i][j]), flagH) # 가로에 필요한 모니터 개수
        rflagV = max(math.ceil(demandMonitor[j] / myMonitor[i][j+1 if j <=4 else None]), rflagV)  # 세로에 필요한 모니터 개수
        #print('짝수 ', j, flagH, rflagV,  '피연산자 ', demandMonitor[j], '연산자', myMonitor[i][j+1 if j <=4 else None])
    for k in range(1, 4, 2):
        flagV = max(math.ceil(demandMonitor[k] / myMonitor[i][k]), flagV) # 세로에 필요한 모니터 개수
        rflagH = max(math.ceil(demandMonitor[k] / myMonitor[i][k-1 if k > 0 else None]), rflagH)  # 세로에 필요한 모니터 개수
        #print('홀수', k, flagV, rflagH, '피연산자 ', demandMonitor[k], '연산자', myMonitor[i][k-1 if k > 0 else None])
    diffPrice.append(myMonitor[i][4] * int(flagH) * int(flagV))
    diffPrice.append(myMonitor[i][4] * int(rflagV) * int(rflagH))
    #print('입력', diffPrice)
    flagH = 0
    flagV = 0
    rflagH = 0
    rflagV = 0
print(min(diffPrice))