'''
유형 : 수학, 다이나믹프로그래밍
1010 : 다리놓기
Date 2021-07-10
Keywords :
'''
N = int(input())
for i in range(N):
    a_site, b_site = map(int, input().split())
    answer = 1
    for multiple in range(b_site,b_site-a_site,-1):
        answer *= multiple
    for divide in range(a_site,0,-1):
        answer //= divide
    print(answer)


