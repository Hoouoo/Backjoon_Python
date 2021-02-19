data = input().split()

MS = list(set(data[0:2])) # set 을 이용해서 중복 제거 / 0~2 인덱스 값 주입
TK = list(set(data[2:])) # set 을 이요해서 중복 제거 / 2 ~ 인덱스 값 주입

#dic은 dictionary로, dic('R') 의 값은 'P'라는 것을 연결해주는 것과 같은 역할을 해준다.
dic = {
    'R': 'P',
    'P':'S',
    'S':'R'
}


if len(MS) == 1 and dic[MS[0]] in TK: # MS의 길이는 set을 이용해서 개수를 줄였으므로 만약 R R 을 냈으면 1 이될 것, 이후 dic[민수의 값]에 대칭되는 값이 TK에 포함되면
        print("TK")
elif len(TK) == 1and dic[TK[0]] in MS:
        print("MS")
else:
    print("?")