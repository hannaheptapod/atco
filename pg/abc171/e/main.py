N = int(input())
a = list(map(int, input().split()))

b = 0
for ai in a: b ^= ai

ans = [b^ai for ai in a]
print(*ans)
