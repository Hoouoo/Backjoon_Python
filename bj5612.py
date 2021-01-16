M = int(input())
N = int(input())
tunnel_in = tunnel_out = final = cnt = ans = 0
for i in range(M):
    tunnel_in, tunnel_out = map(int, input().split())
    N += tunnel_in - tunnel_out
    ans = N if ans < N else ans
    if N < 0:
        cnt += 1
if cnt > 0:
    print(0)
else:
    print(ans)
