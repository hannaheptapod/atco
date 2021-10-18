n = int(input())
a, b, c = map(int, input().split())
ans = 10000
for i in range(10000):
    if ans < i:
        break
    ai = a * i
    for j in range(10000 - i):
        if ans < i + j:
            break
        bj = b * j
        r = n - ai - bj
        if r >= 0 and r%c == 0:
            ijk = i + j + r//c
            ans = min(ans, ijk)
print(ans)