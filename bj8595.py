import re
N = int(input())
arr = input()
ans = re.split("[a-zA-Z]", arr) # 숫자만 추출
#print(ans)
ans = list(map(int, filter(lambda x: x != '', ans))) #split 한 것중 공백 제거
print(sum(ans))