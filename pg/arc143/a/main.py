arr = sorted(map(int, input().split()))

ans = -1 if arr[0] < arr[2]-arr[1] else arr[2]
print(ans)
