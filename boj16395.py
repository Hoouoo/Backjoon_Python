N, K = map(int, input().split())
pascal = [[int(1)] * i for i in range(1, 31)]
for axis1 in range(2, len(pascal)):
    for axis2 in range(1, axis1):
        pascal[axis1][axis2] = pascal[axis1-1][axis2-1] + pascal[axis1-1][axis2]
        # print('#1',pascal[axis1][axis2] )
print(pascal[N-1][K-1])