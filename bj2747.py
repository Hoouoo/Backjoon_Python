num = int(int(input()))
first = F = 0
last = 1
for i in range(0, num+1):
    F += first
    first = last
    last = F
print(F)