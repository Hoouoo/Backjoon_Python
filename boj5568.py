'''
date : 2021-02-16
boj5568

# 자료구조, 브루트포스 알고리즘, 재귀, 해시를 사용한 집합과 맵
'''
from itertools import permutations

n = int(input())
k = int(input())
cards = [input() for _ in range(n)]
ans = set()
for idx in permutations(cards, k):
    ans.add(''.join(idx))
print(len(ans))