S = input()
a, b = map(int, input().split())

arr = list(S)
arr[a-1], arr[b-1] = arr[b-1], arr[a-1]
ans = ''.join(arr)

print(ans)
