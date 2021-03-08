N, M, V = map(int,input().split())
MAP = [[0] * (N + 1) for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    MAP[a][b] = MAP[b][a] = 1
flag = [0] * (N + 1)
def dfs(V):
    flag[V] = 1 # 방문한 곳은 1
    print(V, end=' ')
    for i in range(1, N+1):
        if flag[i] == 0 and MAP[V][i] == 1:
            dfs(i)

def bfs(V):
    queue=[V] #들려야 할 정점 저장
    flag[V]=0 #방문한 점 0으로 표시
    while queue:
        V=queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if flag[i]==1 and MAP[V][i]==1:
                queue.append(i)
                flag[i]=0
dfs(V)
print()
bfs(V)
