'''
유형 : 그리디 알고리즘
2217 : 로프
Date 2021-07-10
Keywords : N번째로 큰 로프를 N번 만큼 곱하기
'''
N = int(input())
rope_types = list(int(input()) for i in range(N))
rope_types.sort(reverse=True)
rope_maxCase = list()
for rope in range(N):
    rope_maxCase.append(rope_types[rope] * (rope+1))
print(max(rope_maxCase))