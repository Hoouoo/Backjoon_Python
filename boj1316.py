'''
유형 : 수학, 문자열
1316 : 그룹 단어 체커
Date 2021-07-17
Keywords : 단어가 떨어져 있는 경우 하나의 그룹으로 취급하지 않는다.
'''

answer = 0
for _ in range(int(input())):
    str_input = input()
    error = 0
    for i in range(len(str_input)-1):
        if str_input[i] != str_input[i+1]:
            check = str_input[i+1 : ]# 현재 글자 이후 글자 탐색
            if check.count(str_input[i]) > 0:
                error += 1
    if error == 0:
        answer += 1
print(answer)




