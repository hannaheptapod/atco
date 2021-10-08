n = int(input())
k = int(input())
x = list(map(int, input().split()))
ans = 0
for xi in x: ans += min(xi, abs(xi - k)) * 2
print(ans)