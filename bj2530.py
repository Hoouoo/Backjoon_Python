Hour, Minute, Second = map(int,input().split()) # list 사용 시 런타임 에러 뜸
needTime = int(input())

Second += needTime % 60 # 초
needTime //= 60
if Second >= 60:
    Second -= 60
    Minute += 1

Minute += needTime % 60 #분
needTime //= 60
if Minute >= 60:
    Minute -= 60
    Hour += 1

Hour += needTime % 24
if Hour >= 24:
    Hour -= 24
print(Hour, Minute, Second)