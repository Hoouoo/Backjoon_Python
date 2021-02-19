a,b,c = map(int, input().split())
change = a + b
remain = 0
while change >= c:
    remain += change // c
    change = change // c + change % c
print(remain)
