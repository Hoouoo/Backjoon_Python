flag = [True] * 11  # range 1 - 10
while True:
    olly = int(input())
    if olly == 0:
        quit()
    stan = input()
    if stan == 'too low':
        for idx in range(0, olly+1):
            flag[idx] = False
    elif stan == 'too high':
        for idx in range(olly, 11):
            flag[idx] = False
    else: # == 'right on'
        if flag[olly]:
            print('Stan may be honest')
            flag = [True] * 11  # range 1 - 10
        else:
            print('Stan is dishonest')
            flag = [True] * 11  # range 1 - 10