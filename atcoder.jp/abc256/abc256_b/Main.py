N = int(input())
A = list(map(int, input().split()))

arr = [0]*4
p = 0
for ai in A:
    arr[0] += 1

    nxt = [0]*4
    for i in range(0, 4-ai): nxt[i+ai] = arr[i]
    for i in range(4-ai, 4): p += arr[i]

    arr = nxt

print(p)
