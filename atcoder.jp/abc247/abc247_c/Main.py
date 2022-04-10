N = int(input())

s = []
for i in range(1, N+1): s = s + [i] + s

print(*s)
