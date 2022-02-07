n = int(input())
a = [0] + list(map(int, input().split()))
b = [0]*(n+1)
ans = [0, []]

for i in range(n, 0, -1):
    if sum(b[2*i::i])%2 == a[i]: b[i] = 0
    else: b[i] = 1

print(sum(b))
if sum(b): print(*[i for i in range(1, n+1) if b[i]])