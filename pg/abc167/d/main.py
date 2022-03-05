import array

N, K = map(int, input().split())
A = [-1] + list(map(int, input().split()))

arr = array.array('i', [1])
now, cnt = 1, 1
while True:
    if A[now] in arr:
        id = arr.index(A[now])
        break

    arr.append(A[now])
    now = A[now]
    cnt += 1

print(arr[id + (K - id)%(len(arr) - id)])
