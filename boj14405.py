'''
14405 : 피카추
Date 2021-07-04

구현 : 문자열
keyword:
피카추는 "pi", "ka", "chu" 만 말할 수 있다.
'''

S = input()
while True:
    if S[0:2] == "pi":
        S = S[2:]
        continue
    elif S[0:2] == "ka":
        S = S[2:]
        continue
    elif S[0:3] == "chu":
        S = S[3:]
        continue

    if len(S) == 0:
        print("YES")
        break
    else:
        print("NO")
        break
