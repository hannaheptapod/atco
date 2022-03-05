N = int(input())
K = list(map(int, input().split()))

l = [K[0]]
for i in range(N-2): l.append(min(K[i], K[i+1]))
l.append(K[-1])

print(*l)
