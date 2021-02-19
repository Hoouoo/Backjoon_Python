# *log, = eval(int(input()) * 'input().split(), ')
# ans = []
# diff = set()
# for name, state in log:
#     diff.add(name)
# # print(diff)
# for name, state in log:
#     cnt = 0
#     for loopName, loopState in log:
#         if name != loopName:
#             cnt += 1
#             if cnt == len(diff): # remove overlap list same cnt
#                 ans.append(name)
#                 # print(ans)
# for output in ans:
#     print(output)
import sys
input
N = int(input())
ans = dict()
for idx in range(N):
    name, state = map(str, input().split())
    if state == "enter":
        ans[name] = True
        # print('#1', ans)
    else:
        del ans[name]
        # print('#2', ans)
ans = sorted(ans.keys(), reverse=True)
for name in ans:
    print(name)