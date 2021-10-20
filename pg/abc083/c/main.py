x, y = map(int, input().split())

ans = 1
a = x

while a*2 <= y:
    a *= 2
    ans += 1

print(ans)