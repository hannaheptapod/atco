n = int(input())
h = list(map(int, input().split()))
m = h[0]
m += sum(h[i + 1] - h[i] for i in range(n - 1) if h[i + 1] > h[i])
print(m)