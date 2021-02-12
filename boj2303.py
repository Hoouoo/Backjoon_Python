import itertools as it

case = int(input())
testcase = [list(map(int, input().split())) for _ in range(case)]
result = []
for i in range(len(testcase)):
    stack = []
    for combi in it.combinations(testcase[i], 3):
        #print(combi)
        stack.append(sum(list(combi)) % 10)
        #print(stack)
    #stack.sort(reverse=True) # reverse = True
    #result.append(stack[0])
    result.append(max(stack))
    #print(result)
num = max(result)
numy = []
for j in range(len(result)):
    if result[j] == num:
        numy.append(j)
print(max(numy)+1)