N, X, Y = map(int, input().split())

arr = [[0, 0] for _ in range(N-1)] + [[1, 0]]
for i in range(N-1, 0, -1):
    arr[i-1][0] += arr[i][0]
    arr[i][1] += arr[i][0]*X
    arr[i-1][0] += arr[i][1]
    arr[i-1][1] += arr[i][1]*Y

print(arr[0][1])
